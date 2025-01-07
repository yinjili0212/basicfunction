import dmPython
# import pandas as pd

#连接数据库
conn=dmPython.connect(user='ECS', password='ecs123', server='10.128.231.57', port=5236)
#创建游标
cursor=conn.cursor()

#执行语句
cursor.execute("select * from t_bms_order_records")
res=cursor.fetchall()
print(res)
#关闭游标
cursor.close()
#关闭数据库连接
conn.close()
