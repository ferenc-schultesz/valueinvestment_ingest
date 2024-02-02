from sqlalchemy import create_engine
import urllib
import pandas as pd
from config import DB_SERVER, DATABASE_NAME, DB_USERNAME, DB_PASSWORD

def insert_to_db(schema, table_name, data: pd.DataFrame):    
    SERVER = DB_SERVER
    DATABASE = DATABASE_NAME
    USERNAME = DB_USERNAME
    PASSWORD = DB_PASSWORD

    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

    # Create the connection string
    params = urllib.parse.quote_plus(connectionString)

    # Create the SQLAlchemy engine
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

    # Write the DataFrame to the SQL Server table
    data.to_sql(table_name, con=engine, schema=schema, if_exists='append', index=False)