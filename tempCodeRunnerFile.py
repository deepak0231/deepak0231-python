
import cx_Oracle
conn = cx_Oracle.connect('library_test1/library@//localhost:1521/xe')
print(conn.version)