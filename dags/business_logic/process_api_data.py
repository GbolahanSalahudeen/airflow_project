import json
import pandas as pd

raw_path = '/opt/airflow/dags/data/stock_data.json'
transformed_path = '/opt/airflow/dags/data/processed_stock_data.csv'

def process_stock_data():
    '''
    Process the extracted stock data

    Returns:
        Transformed csv file containing data to be loaded to database
    '''
    with open(raw_path, 'r') as file:
        data = json.load(file)

    df = pd.DataFrame(data)

    # filter to contain only market data with ffrequency greater than 0
    df_filter = df[df['frequency'] > 0]

    df_filter.to_csv(transformed_path, index=False)

