from oracleDBHandle import OracleDBHandler
#建立数据库连接
o = OracleDBHandler(user='PERU_BMS', password='Zpmc#3261', dsn='10.128.231.88:1521/PERU_PRODUCT_DB')

# #测试query函数
# results = o.query("select * from T_BMS_ASC_COMMAND")
# for result in results:
#     print(result)

################
# #测试getData函数1
# results = o.getData(table='T_BMS_ASC_COMMAND', fields='TASK_STATUS', conditions=None)
# for result in results:
#     print(result)

# ###############
# #测试getData函数2
# results = o.getData(table='T_BMS_ASC_COMMAND', fields='TASK_STATUS', conditions="TASK_STATUS='COMPLETED'")
# for result in results:
#     print(result)

# #测试updateTable函数
# o.updateTable(table='T_BMS_ASC_COMMAND', fields='ORDERVERSION', values="2",conditions="AORID=154224685")
#

# #测试delData函数
# o.delData(table='T_BMS_ASC_COMMAND', conditions="AORID=154224685")

# #测试executesql函数,一般用来更新和删除数据信息
# o.executesql("delete from T_BMS_ASC_COMMAND where AORID=154225250")


#关闭数据库和游标连接
o.close()






