
from constants import *

import pandas as pd
from datetime import datetime

from etl_pipeline.extract import *
from etl_pipeline.transform import *
from etl_pipeline.load import *

if __name__ == '__main__':
    data = extract_restaurants_data()
    countries = pd.read_excel('./data_files/Country-Code.xlsx')
    print("Start scraping")
    d_countries = extract_countries_data(countries)
    restaurant_records = extract_restaurant_records_from_parsed_json(data)
    df = parse_restaurant_records_into_df(d_countries, restaurant_records)
    df = process_event_data_for_restaurants(df)
    q1_df = prepare_data_for_q1(df)    
    q2_df = prepare_data_for_q2(df)

    curr_time = datetime.now()
    q1_filename = f"sample_output/q1_{curr_time}.csv"
    q2_filename = f"sample_output/q2_{curr_time}.csv"

    q1_df.to_csv(q1_filename)
    q2_df.to_csv(q2_filename)
    print("done")





