import oracledb
conn = oracledb.connect(user='PERU_BMS', password='Zpmc#3261', dsn='10.128.231.88/PERU_PRODUCT_DB')
#创建游标
cur = conn.cursor()

#查询数据
cur.execute("select NAME,VALUE,DESCRIPTION,UPDATE_TIME from T_BMS_LANGUAGE_MAP_TEST order by NAME asc")
results = cur.fetchall()
for result in results:
    # print(type(result))
    print(f'''INSERT INTO T_BMS_LANGUAGE_MAP(NAME, VALUE, DESCRIPTION, UPDATE_TIME)VALUES('{result[0]}','{result[1]}','{result[2]}',NULL);''')
conn.close()