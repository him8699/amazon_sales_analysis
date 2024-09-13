import pandas as pd
from sqlalchemy import create_engine

df=pd.read_csv('amazon.csv')
db_url = "postgresql://postgres:.......@localhost:5432/amazon_sales"
engine=create_engine(db_url)
df.to_sql('amazon_sales',engine,if_exists='replace',index=False)