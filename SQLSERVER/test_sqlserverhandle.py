from sqlserverHandle import SqlserverHandler

#连接数据库
o = SqlserverHandler(host='10.128.254.113',user='ECS',password='Zpmc@254.113',service_name='HIT_Alarm')
# #打印连接信息
# print(o)

#查询数据1
results = o.query("select * from dbo.rcms_alarm")
for result in results:
    print(result)
# #查询数据2
# results = o.getData(table='dbo.rcms_alarm', fields='alarm_id,description', conditions="alarm_id in ('1','2')")
# for result in results:
#     print(result)

# ##删除数据,
# #按照条件删除数据
# # o.delData(table='dbo.rcms_alarm_log', conditions="id=441324")
# # #整表删除数据
# o.delData(table='dbo.rcms_alarm_log')

# #插入数据
# o.executesql("insert into dbo.rcms_alarm_log (alarm_id,alarm_code,alarm_on_time,alarm_off_time,alarm_duration,crane_id,alarm_log_id) values (1,0,'2022-06-25 21:14:33.320','2022-06-25 21:14:33.320',3,1,1)")
o.close()
