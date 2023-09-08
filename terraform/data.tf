data "archive_file" "restaurant_lambda_file" {
  type = "zip"

  source_dir  = "../lambda"
  output_path = "../lambda.zip"
}


data "archive_file" "lambda_layer" {
  type = "zip"

  source_dir  = "../lambda"
  output_path = "../lambda.zip"
}

