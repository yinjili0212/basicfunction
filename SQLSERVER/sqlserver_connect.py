
# # #################################################方法1：使用pymssql模块连接SQLSERVER数据库
# import pymssql #导入模块
# #创建连接
# connect = pymssql.connect('10.128.254.113','ECS','Zpmc@254.113','HIT_Alarm')  #connect = pymssql.connect('服务器名称', '用户名', '密码', '库名')  # 建立连接
# if connect:
#     print(connect)
#     print("连接成功")
# cursor = connect.cursor()
# sql = "select * from dbo.rcms_alarm"
# cursor.execute(sql)
# row = cursor.fetchone()
# while row:
#     print(row)
#     row = cursor.fetchone()
# cursor.close()
# connect.close()


# # #################################################方法2：使用pyodbc连接SQLSERVER数据库
# import pyodbc
# # 连接数据库
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.128.254.113;DATABASE=HIT_Alarm;UID=ECS;PWD=Zpmc@254.113')
# # 创建游标
# cursor = cnxn.cursor()
# # 查询数据
# cursor.execute("SELECT *  FROM dbo.rcms_alarm")
# row = cursor.fetchone()
# rows = cursor.fetchall()
# print(row)#获取单行数据
# print(rows)#获取全部数据
# # print(rows)
# # 关闭游标和连接
# cursor.close()
# cnxn.close()

# #################################################方法1：使用pymssql模块连接SQLSERVER数据库
import pymssql #导入模块
#创建连接
connect = pymssql.connect('10.128.231.79','rcmsdb.user','Pr0RSq@19-123','ECSDB-OMAN')  #connect = pymssql.connect('服务器名称', '用户名', '密码', '库名')  # 建立连接
if connect:
    print(connect)
    print("连接成功")
# cursor = connect.cursor()
# sql = "select * from dbo.rcms_alarm"
# cursor.execute(sql)
# row = cursor.fetchone()
# while row:
#     print(row)
#     row = cursor.fetchone()
# cursor.close()
connect.close()