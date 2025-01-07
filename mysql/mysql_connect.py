import mysql.connector
mydb = mysql.connector.connect(
  host="10.128.231.131",
  user="root",
  password="Zpmc@231.131",
  database="bms_db1"
)
# print(mydb)#打印数据库是否连接上

#创建游标
cur = mydb.cursor()

#从数据库查询数据
query = "SELECT * FROM t_bms_system_config"
cur.execute(query)
#查询结果显示，不显示字段名称
myresults = cur.fetchall()
for x in myresults:
    print(x)


#显示字段名称
fields = cur.description
for field in fields:
    print(field[0])

# mycursor.close()
mydb.close()
