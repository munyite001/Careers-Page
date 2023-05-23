import os
from sqlalchemy import create_engine

#   Establish connection to database
try:
    engine = create_engine(os.environ.get('DB_CONNECTION_STRING'))
    print("Connection succeeded successfully")
except Exception as ex:
    print(f"Connection couldn't be made due to the following error: {ex}")
