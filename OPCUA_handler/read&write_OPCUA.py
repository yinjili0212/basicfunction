from opcua import Client
# #-----------------------------------------读取OPCUA的值和写入OPCUA的值
client = Client("opc.tcp://10.128.231.170:5600/")
client.connect()

# 读取变量的值
var = client.get_node("ns=1;s=QCMS_ACCS.QC901.PLC_OPC.PfStatus")#OPC点的地址
value = var.get_value()
print(type(value))#打印OPC点数值
#
#
# # # 设置变量的值
# var.set_value(1)#注意写入的OPC点类型是string还是Int
# # 断开OPC UA客户端连接
# client.disconnect()



