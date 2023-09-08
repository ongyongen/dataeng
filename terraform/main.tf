# Create S3 bucket to store the lambda zip file
resource "aws_s3_bucket" "restaurants_output_bucket" {
  bucket = "restaurants-output-bucket"
}

# Configure S3 bucket to allow allow access via cloudfront
resource "aws_s3_bucket_public_access_block" "restaurants_output_bucket" {
  bucket = aws_s3_bucket.restaurants_output_bucket.id

  block_public_acls = false
  block_public_policy = false
  ignore_public_acls = false
  restrict_public_buckets = false
}

# Create S3 bucket to store the lambda zip file
resource "aws_s3_bucket" "restaurants_input_bucket" {
  bucket = "restaurants-input-bucket"
}

resource "aws_s3_object" "restaurants_lambda_object" {
  bucket = aws_s3_bucket.restaurants_input_bucket.id

  key    = "lambda.zip"
  source = data.archive_file.restaurant_lambda_file.output_path

  etag = filemd5(data.archive_file.restaurant_lambda_file.output_path)
}

# Create an IAM role for the scraper lambda function 
resource "aws_iam_role" "restaurants_lambda_role" {
  name = "restaurant-lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}


data "aws_iam_policy_document" "restaurants_lambda_policy" {
  statement {
    effect    = "Allow"
    actions   = [
      "s3:PutObject"
    ]
    resources = ["*"]
  }
}

resource "aws_iam_policy" "restaurants_lambda_policy" {
  name        = "restaurants-lambda-policy"
  description = "A test policy"
  policy      = data.aws_iam_policy_document.restaurants_lambda_policy.json
}

resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = aws_iam_role.restaurants_lambda_role.name
  policy_arn = aws_iam_policy.restaurants_lambda_policy.arn
}


# Create an AWS Lambda Layer using the ZIP file
resource "aws_lambda_layer_version" "restaurants_lambda_layer" {
  layer_name = "restaurants_lambda_layer"  # Name for your Lambda Layer
  compatible_runtimes = ["python3.8"]  # List of compatible runtimes

  # Specify the ZIP file for your layer
  filename = "../lambda/layers/python.zip"
}


# Create the lambda function to scrape the geocaches
resource "aws_lambda_function" "restaurants_lambda_function" {
  function_name = "restaurant-lambda-function"
  
  s3_bucket = aws_s3_bucket.restaurants_input_bucket.id
  s3_key    = aws_s3_object.restaurants_lambda_object.key

  role          = aws_iam_role.restaurants_lambda_role.arn
  handler       = "lambda_function.lambda_handler"  

  runtime = "python3.7"  
  source_code_hash = data.archive_file.restaurant_lambda_file.output_base64sha256

  timeout = 200
  
  
  layers = [
     var.python37_layer_arn, 
     aws_lambda_layer_version.restaurants_lambda_layer.arn 
  ]
}

# Connect lambda function to an EventBridge (run lambda function Mon to Fri 5pm)
resource "aws_cloudwatch_event_rule" "restaurants_lambda_event_rule" {
  name = "geotrails-scraper-lambda-event-rule"
  description = "retry scheduled every 2 min"
  schedule_expression = "cron(0 17 ? * MON-FRI *)"
}

resource "aws_cloudwatch_event_target" "profile_generator_lambda_target" {
  arn = aws_lambda_function.restaurants_lambda_function.arn
  rule = aws_cloudwatch_event_rule.restaurants_lambda_event_rule.name
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_rw_fallout_retry_step_deletion_lambda" {
  statement_id = "AllowExecutionFromCloudWatch"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.restaurants_lambda_function.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.restaurants_lambda_event_rule.arn
}