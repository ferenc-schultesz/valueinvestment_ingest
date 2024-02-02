# Things that this needs..

- Needs ODBC 18 or need to change the driver name in `db_helper.py`
- Need a `config.py` in root with the following structure:

```
valueinvesting_api_key = ''
DB_SERVER = ''
DATABASE_NAME = ''
DB_USERNAME = ''
DB_PASSWORD = ''
```

- Then you can set the stock symbol on the top of the `main.py`for whatever stock you want to get and run it