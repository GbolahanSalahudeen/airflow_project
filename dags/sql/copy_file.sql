COPY bronze.crm_cust_info
FROM '{{params.csv_path_1}}'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');

COPY bronze.crm_prd_info
FROM '{{params.csv_path_2}}'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');

COPY bronze.crm_sales_details
FROM '{{params.csv_path_3}}'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');

COPY bronze.erp_cust_az
FROM '{{params.csv_path_4}}'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');

COPY bronze.erp_loc
FROM '{{params.csv_path_5}}'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');

COPY bronze.erp_px_cat
FROM '{{params.csv_path_6}}'
WITH (FORMAT CSV, HEADER true, DELIMITER ',');