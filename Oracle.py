
import cx_Oracle
conn = cx_Oracle.connect('library_test1/library@//localhost:1521/xe')
print(conn.version)

# Create Cursor
cur = conn.cursor()

sql_create = """
select * from kchouse
"""

cur.execute(sql_create)
for line in cur:
    print(line)

print("Table created1")