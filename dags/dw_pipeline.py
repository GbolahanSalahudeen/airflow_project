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
    
    download_s3_files = PythonOperator(
        task_id='s3_download_files',
        python_callable=s3_download_file,
        op_kwargs={
            'bucket_name': 'dw-dataset-bucket',
            'object_key': 'sales_data/',
            'path': '/opt/airflow/dags/data/s3_files'
        }
    )
    
    # extract_data = SQLExecuteQueryOperator(
    #     task_id='fetch_s3_data_to_postgres',
    #     sql='''
    #         COPY landing.customers
    #         FROM 's3://cde-capstone-olalekan/customers'
    #         IAM_ROLE 'arn:aws:iam::068355631913:role/capstone-redshift-role'
    #         FORMAT AS PARQUET
    #         '''
    # )

    download_s3_files
    
    