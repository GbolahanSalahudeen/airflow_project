import requests
import json
from airflow.models import Variable

api_key = Variable.get('API_KEY')
url = f'https://api.massive.com/stocks/v1/dividends?limit=100&sort=ticker.asc&apiKey={api_key}'
file_path = '/opt/airflow/dags/data/stock_data.json'

def get_stock_data():
    '''
    Fetches stock data from massive.com

    Returns:
        Stock data in json format
    '''
    response = requests.get(url)
    data = response.json()
    results = data.get('results')
    
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)