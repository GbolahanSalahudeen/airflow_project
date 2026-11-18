from sqlalchemy import create_engine, text
import os
import pandas as pd

file_path = '/opt/airflow/dags/data/processed_stock_data.csv'
table_name = 'stock_market'

postgres_host = 'postgres'
postgres_user = 'airflow'
postgres_password = 'airflow'
postgres_db = 'stock_db'
port = 5432

conn_string = f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{port}/{postgres_db}'

def load_stock_db():
    '''
    Load processed stock data into PostgreSQL datawarehouse
    '''
    engine = create_engine(conn_string)
    df = pd.read_csv(file_path)
    df.to_sql(table_name, con=engine, if_exists='append', schema='public', index=False)