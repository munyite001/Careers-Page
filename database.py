import os
from sqlalchemy import create_engine, text

#   Establish connection to database
try:
    engine = create_engine(os.environ.get('DB_CONNECTION_STRING'))
    print("Connection succeeded successfully")
except Exception as ex:
    print(f"Connection couldn't be made due to the following error: {ex}")


def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

        #   Convert Sql Alchemy Legacy row to list of dictionaries
        result_dict = []

        for res in result.all():
            result_dict.append(dict(res))
    return result_dict

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val").bindparams(val=id))
        
        rows = result.all()

        if len(rows) == 0:
            return None
        else:
            return (dict(rows[0]))

