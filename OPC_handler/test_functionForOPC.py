from functionForOPC import opc_read,opc_write

#读取OPC点
results = opc_read(tags=['BMS_ACCS.B0101.OPC_PLC.HeartBeat','BMS_ACCS.B0101.OPC_PLC.HTSChassisPosition'],ip='localhost')
print(results)

#写入OPC点
opc_write(tags={'BMS_ACCS.B0101.OPC_PLC.HeartBeat':20,'BMS_ACCS.B0101.OPC_PLC.HTSChassisPosition':10},ip='localhost')
