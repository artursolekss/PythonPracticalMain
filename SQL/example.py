import pandas as pd
import pymysql

from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine("mysql+pymysql://root:@localhost/myshop")


with engine.begin() as con:
    query = text("SELECT * FROM supplier")
    suppliers_df = pd.read_sql(query,con)

print(suppliers_df)
