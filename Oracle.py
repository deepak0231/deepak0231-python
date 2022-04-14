import cx_Oracle
import pandas as pd
conn = cx_Oracle.connect('library_test1/library@//localhost:1521/xe')
print(conn.version)

# Create Cursor
cur = conn.cursor()

sql_create = """
select * from kchouse
"""

cur.execute(sql_create)
# for line in cur:
#     print(line)

print("Table created1")
df = pd.DataFrame(cur, columns=['id','date','price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15'])
print(df.head())
print("Table created2")