import requests
from utils import flatten_json, create_dataframe_for_stock_data_table
from db_helper import insert_to_db
from config import valueinvesting_api_key

# this is what we are getting and inserting to db
STOCK_SYMBOL = 'MSFT'

# get data from API for stock symbol
response = requests.get(f'https://valueinvesting.io/api/valuation?tickers={STOCK_SYMBOL}&api_key={valueinvesting_api_key}')

# get the content from the API response and flatten it
flattened_json = flatten_json(response.content)

# create a pandas dataframe from the json that matches the columns in db
stock_dataframe = create_dataframe_for_stock_data_table(flattened_json, STOCK_SYMBOL)

# insert to db
insert_to_db(schema='dbo', table_name='StockData', data=stock_dataframe)