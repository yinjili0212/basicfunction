from mysqldbHandle import MysqldbHandler
o = MysqldbHandler(host='10.128.254.42',user='root',password='123456',database='xxl_job')
#查询数据表
results = o.query("select * from xxl_job_info")
for result in results:
    print(result)

# #根据指定条件查询字段名和where条件
# results = o.getData(table='xxl_job_info', fields='id,job_group', conditions=None)
# for result in results:
#     print(result)

# #更新数据库
# o.executesql("update xxl_job_info_copy1 set alarm_email='wer',job_desc='ert',author='er' where id='8'")

# #删除数据
# o.delData(table='xxl_job_info_copy1',conditions="id='8'")
o.close()