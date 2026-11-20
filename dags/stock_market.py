from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from pendulum import datetime
from datetime import timedelta
from business_logic.get_api_data import get_stock_data
from business_logic.process_api_data import process_stock_data
from business_logic.load_db import load_stock_db

default_args = {
    'owner': 'gbolahan',
    'email': ['salahudeengbolahan10@gmail.com'],
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}


with DAG(
    dag_id='stock_market_pipeline',
    description='Fetch stock market data and process it for application',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule='@daily',  # runs every 5am daily
    catchup=False,
    tags=['de-class', 'stock-market']
):
    
    extract_stock_data = PythonOperator(
        task_id='fetch_stock_data',
        python_callable=get_stock_data
    )
    
    process_data = PythonOperator(
        task_id='transform_stock_data',
        python_callable=process_stock_data
    )

    load_db = PythonOperator(
        task_id='load_stock_database',
        python_callable=load_stock_db
    )

    # set dependency
    extract_stock_data >> process_data >> load_db