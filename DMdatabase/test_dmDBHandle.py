from dmDBHandle import DmDBHandler

#建立数据库连接
o = DmDBHandler(user='ECS',password='ecs123',server='10.128.231.57',port=5236)

# #测试query函数
# results = o.query("select * from t_bms_order_records")
# for result in results:
#     print(result)

# #测试getData函数1
# results = o.getData(table='t_bms_order_records', fields='ORDER_CATEGORY,ORDER_ID,ORDER_TYPE,ORDER_STATUS', conditions=None)
# for result in results:
#     print(result)

# #测试getData函数2
# results = o.getData(table='t_bms_order_records', fields='ORDER_CATEGORY,ORDER_ID,ORDER_TYPE,ORDER_STATUS', conditions="ORDER_ID=16406020080452608")
# for result in results:
#     print(result)

# #测试updateTable函数
# o.updateTable(table='t_bms_order_records', fields='ORDER_STATUS', values="'COMPLETE'",conditions="ORDER_ID=20230712153422")


# #测试delData函数
# o.delData(table='t_bms_order_records', conditions="ORDER_ID=20230713155446")

# #测试executesql函数,一般用来更新和删除数据信息
# o.executesql("delete from t_bms_order_records where ORDER_ID=20230713155128")

# #测试executemany函数,一般用来更新和删除数据信息
# o.executemany("delete from t_bms_order_records where ORDER_ID=20230713152516;delete from t_bms_order_records where ORDER_ID=16406020080452608;")

#关闭数据库和游标连接
o.close()