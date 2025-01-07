import OpenOPC
import datetime
import pywintypes
pywintypes.datetime = pywintypes.TimeType
def opc_read(tags,ip='localhost'):#读OPC点的函数,tags=['点1','点1']
    # 连接远程的OPC服务器
    opc = OpenOPC.client()
    opc.connect('ZPMC.OPCServer.2', ip)
    if len(tags) != 0:#当查询的OPC点大于1个点
        results_list = []
        results = opc.read(tags)#输出的是[('OPC点1', 0, 'Good', '2023-05-06 06:33:16.142000+00:00'), ('OPC点2', 0, 'Good', '2023-05-06 06:33:16.142000+00:00')]
        # time_local = datetime.datetime.strptime(results[0][3][0:26], '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(hours=8)  # 将读取到的时间+8小时作为北京时间
        time_local = datetime.datetime.strptime(results[0][3][0:19], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)  # 将读取到的时间+8小时作为北京时间
        for result in results:
            spot_1 = []#创建一个空list，目的是传统读取的OPC点的时间是utc时间，比北京时间少8小时，转换为正常可读的时间
            spot_1.append(result[0])#result[0]表示OPC点的名称
            spot_1.append(result[1])#result[1]表示OPC点的值
            spot_1.append(result[2])#result[2]表示OPC点的质量
            spot_1.append(str(time_local))#读取的OPC最后一次更新的时间
            results_list.append(spot_1)
        return results_list
    # 关闭opc连接
    opc.close()
def opc_write(tags,ip='localhost'):#写OPC点的函数{'PCMS_RCCS.RCCS.PC01.PCMS_RCCS.IgvFollowResult':20,'PCMS_RCCS.RCCS.PC01.PCMS_RCCS.LockIgvResult':10},'10.128.254.233'
    #链接远程的OPC服务器
    opc = OpenOPC.client()
    opc.connect('ZPMC.OPCServer.2',ip)
    if len(tags) !=0:#当写入的点不为0
        results_list = []
        for i in tags.items():#输出的格式正好是opc.write需要的格式[('OPC点1'，值1),('OPC点2'，值2)]
            results_list.append(i)
        opc.write(results_list)
    #关闭opc连接
    opc.close()