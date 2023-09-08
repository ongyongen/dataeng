import json
import pandas as pd

from constants import *

import pandas as pd
from datetime import datetime

from etl_pipeline.extract import *
from etl_pipeline.transform import *
from etl_pipeline.load import *

from json import loads
import awswrangler as wr

def lambda_handler(event, context):

    data = extract_restaurants_data()
    countries = pd.read_excel('./data_files/Country-Code.xlsx')
    d_countries = extract_countries_data(countries)
    restaurant_records = extract_restaurant_records_from_parsed_json(data)
    df = parse_restaurant_records_into_df(d_countries, restaurant_records)
    df = process_event_data_for_restaurants(df)
    q1_df = prepare_data_for_q1(df)
    q2_df = prepare_data_for_q2(df)
    
    curr_time = datetime.now()
    q1_filename = f"q1_{curr_time}.csv"
    q2_filename = f"q2_{curr_time}.csv"


    filepath_q1 = f"s3://restaurants-output-bucket/{q1_filename}"
    filepath_q2 = f"s3://restaurants-output-bucket/{q2_filename}"

    wr.s3.to_csv(df=q1_df,path=filepath_q1)
    wr.s3.to_csv(df=q2_df,path=filepath_q2)

    return {
        'statusCode': 200,
        'body': json.dumps('All Singapore Geocaches are scraped!')
    }


