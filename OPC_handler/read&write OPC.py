
#***************************************登录本机OPC服务器且读写点
# # 导入OPC读取相关库
# import OpenOPC
# import pywintypes
# import datetime
# pywintypes.datetime = pywintypes.TimeType
# # 连接本机的OPC服务器
# opc = OpenOPC.client()
# opcserv = 'ZPMC.OPCServer.2'
# opc.connect(opcserv)
# #打印连接信息
# print(opc.info())
# # # ============read one tag ================
# # ============read one tag ================
# tag =['BMS_ACCS.B0101.OPC_PLC.HeartBeat']
# value = opc.read(tag)
# print(value)
# time_local = datetime.datetime.strptime(value[0][3][0:26], '%Y-%m-%d %H:%M:%S.%f')+datetime.timedelta(hours=8)#将读取到的时间+8小时作为北京时间
# print(time_local)
# # # ============读多个点 ================
# tags=['BMS_ACCS.B0101.OPC_PLC.HeartBeat','BMS_ACCS.B0101.OPC_PLC.HTSChassisPosition']
# value = opc.read(tags)
# time_local = datetime.datetime.strptime(value[0][3][0:26], '%Y-%m-%d %H:%M:%S.%f')+datetime.timedelta(hours=8)#将读取到的时间+8小时作为北京时间
# print(value,time_local)
# # ===========写一个点================
# tag ='BMS_ACCS.B0101.OPC_PLC.HeartBeat'
# # #方式1
# opc.write( (tag, 1) )
# value = opc.read([tag])
# print(value)
# # # ===========写多个点================
# opc.write( [('BMS_ACCS.B0101.OPC_PLC.HeartBeat', 20), ('BMS_ACCS.B0101.OPC_PLC.HTSChassisPosition', 0)] )
# tags = ['BMS_ACCS.B0101.OPC_PLC.HeartBeat','BMS_ACCS.B0101.OPC_PLC.HTSChassisPosition']
# value = opc.read(tags)
# print(value)
# # 关闭opc连接
# opc.close()



#***************************************登录远程OPC服务器且读写点
# 导入OPC读取相关库
# import OpenOPC
# import pywintypes
# pywintypes.datetime = pywintypes.TimeType
# # 连接远程的OPC服务器
# opc = OpenOPC.client()
# opc.connect('ZPMC.OPCServer.2', '10.128.254.170')
# #打印连接信息
# print(opc.connect('ZPMC.OPCServer.2', '10.128.254.233'))
# print(opc.info())
# # ============read one tag ================
# # # ============read one tag ================
# uptime = opc.get_uptime()
# print(uptime)
# tag ='ROCS_Buffer.RCS.RCS01.Available'
# value = opc.read(tag)
# print(value)
# # # ============读多个点 ================
# tags=['PCMS_RCCS.RCCS.PC01.PCMS_RCCS.IgvFollowResult','PCMS_RCCS.RCCS.PC01.PCMS_RCCS.HeartBeat']
# value = opc.read(tags)
# print(value)
# # # ===========写一个点================
# tag ='ROCS_Buffer.ASC001.Mode'
# # #方式1
# opc.write( (tag, 20) )
# value = opc.read(tag)
# print(value)
# # # ===========写多个点================
# opc.write( [('ROCS_Memory.ASC001.MSRequestMode', 1), ('ROCS_Memory.ASC001.RemoteJobID', 0)] )
# tags = ['PCMS_RCCS.RCCS.PC01.PCMS_RCCS.IgvFollowResult','PCMS_RCCS.RCCS.PC01.PCMS_RCCS.LockIgvResult']
# value = opc.read(tags)
# print(value)
# # 关闭opc连接
# opc.close()