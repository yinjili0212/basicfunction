import cx_Oracle
#连接数据库
conn = cx_Oracle.connect('nuct_sch/nuctsch123@10.128.254.200/nuct_product_db')
#创建游标
cur = conn.cursor()
#查询数据
cur.execute("select * from aht_status")
results = cur.fetchall()
for result in results:
    print(result)

conn.close()