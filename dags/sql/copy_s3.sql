COPY bronze.crm_cust_info
FROM 's3://dw-dataset-bucket/sales_data/CUST_AZ12.parquet'
IAM_ROLE 'arn:aws:iam::068355631913:role/capstone-redshift-role'
FORMAT AS PARQUET;

COPY bronze.crm_cust_info
FROM 's3://dw-dataset-bucket/sales_data/CUST_AZ12.parquet'
IAM_ROLE 'arn:aws:iam::068355631913:role/capstone-redshift-role'
FORMAT AS PARQUET