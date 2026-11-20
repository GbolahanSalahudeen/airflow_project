from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from pendulum import datetime
from datetime import timedelta
from business_logic.s3_download import s3_download_file


default_args = {
    'owner': 'gbolahan',
    'email': ['salahudeengbolahan10@gmail.com'],
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}


with DAG(
    dag_id='dw_dbt_pipeline',
    description='Load from S3 to Postgres and transform with dbt',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule='@daily',  # runs every 5am daily
    catchup=False,
    tags=['de-class', 'dbt'],
    template_searchpath=["/opt/airflow/dags/sql"]
):
    
    # download_s3_files = PythonOperator(
    #     task_id='s3_download_files',
    #     python_callable=s3_download_file,
    #     op_kwargs={
    #         'bucket_name': 'dw-dataset-bucket',
    #         'object_key': 'sales_data/',
    #         'path': '/opt/airflow/dags/data/s3_files'
    #     }
    # )
    
    extract_data = SQLExecuteQueryOperator(
        task_id='copy_csv_to_postgres',
        conn_id='postgres_default',
        sql='sql/copy_file.sql',
        split_statements=True,
        return_last=False,
        params={
            'csv_path_1': '/opt/airflow/dags/data/s3_files/cust_info.csv',
            'csv_path_2': '/opt/airflow/dags/data/s3_files/prd_info.csv',
            'csv_path_3': '/opt/airflow/dags/data/s3_files/sales_details.csv',
            'csv_path_4': '/opt/airflow/dags/data/s3_files/CUST_AZ12.csv',
            'csv_path_5': '/opt/airflow/dags/data/s3_files/LOC_A101.csv',
            'csv_path_6': '/opt/airflow/dags/data/s3_files/PX_CAT_G1V2.csv'
        }
    )

    extract_data
    
    