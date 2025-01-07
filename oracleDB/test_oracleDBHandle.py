from oracleDBHandle import OracleDBHandler
#建立数据库连接
o = OracleDBHandler(host='10.128.254.200',port=1521,service_name='nuct_product_db',user='nuct_sch',password='nuctsch123')

# #测试query函数
# results = o.query("select * from aht_status")
# for result in results:
#     print(result)

# #测试getData函数1
# results = o.getData(table='aht_status', fields='CHE_ID,OPERATIONAL_STATUS,TECHNICAL_STATUS,TECHNICAL_DETAILS', conditions=None)
# for result in results:
#     print(result)

# #测试getData函数2
# results = o.getData(table='aht_status', fields='CHE_ID,OPERATIONAL_STATUS,TECHNICAL_STATUS,TECHNICAL_DETAILS', conditions="CHE_ID='V001'")
# for result in results:
#     print(result)

# #测试updateTable函数
# o.updateTable(table='aht_cmd_q', fields='STATUS', values="'COMPLETE'",conditions="Q_ID=27026456")


# #测试delData函数
# o.delData(table='aht_cmd_q', conditions="Q_ID=27026456")

# #测试executesql函数,一般用来更新和删除数据信息
# o.executesql("delete from aht_cmd_q where Q_ID=27026573")


#关闭数据库和游标连接
o.close()






