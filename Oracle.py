import cx_Oracle
import pandas as pd
import warnings
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
df = pd.DataFrame(cur, columns=['id','date','price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15'])
# print(df.head())
# print(df.info())
# print(df.describe)
# df.to_excel('Try.xlsx')
df1 = df[['id','date','price','bedrooms']]
print(df1.head())
df2 = df[['bathrooms']]
# print('df2 is:', df2[0])
# print(df2[21609])
# print(df.head(1))
# warnings.filterwarnings('ignore')
# df['sqft_living'][0] = 1175
# print('new:', df.head(1))
# print(df2.values)
# print('Sum is:', df2.sum())
# print(df2.values.sum())
# print('Mean is:', df2.mean())
df1['End'] = df1['bedrooms'] * 10
print(df1.head())
df1.insert(loc= 2, column='New Col', value= df1['price'] * 2)
print(df1.head())