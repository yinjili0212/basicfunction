#打开xls读取贝列层信息，解析后画到新的xls显示箱子
import xlrd
import xlwt
#最终得到可是画的堆场占用图，20尺显示红色，40尺显示绿色
#需要读取的初始文件
init_file = r'block_container_show3.xls'
sheet_name1 = 'datasource'#初始xls存入的数据所在的sheet页
#需要写入的目的文件
target_file = r'block_container_show4.xls'
#步骤1：打开init_file读取数据源,用region和endregion标注代码块
#region
#打开源头xls文件
workbook_init = xlrd.open_workbook(init_file)
#根据指定sheet页名称打开指定sheet页
sheet = workbook_init.sheet_by_name(sheet_name1)
def list_baylanetier(col_index):#将贝列层信息转化为int类型数据
    data_baylanetiers = sheet.col_values(col_index, start_rowx=1, end_rowx=None)
    a = []
    for data_baylanetier in data_baylanetiers:
        a.append(int(data_baylanetier))
    data_baylanetiers = a
    return data_baylanetiers
def list_characterstrings(col_index):#将非int类型数据转化为非int类型数据return，如堆场号和箱号
    data_baylanetiers = sheet.col_values(col_index, start_rowx=1, end_rowx=None)
    a = []
    for data_baylanetier in data_baylanetiers:
        a.append(data_baylanetier)
    data_baylanetiers = a
    return data_baylanetiers

data_bays = list_baylanetier(0)#贝
data_lanes = list_baylanetier(1)#列
data_tiers = list_baylanetier(2)#层
data_containerids = list_characterstrings(3)#箱号，可为空
data_blocks = list_characterstrings(4)#堆场号，不能为空必须给一个堆场号
#endregion
# # ##################################################################填充xls
# 创建一个新的 Workbook 对象
new_workbook = xlwt.Workbook()

blocks = []#将堆场从步骤1中data_blocks中筛选出来，加到block这个list中，只有当堆场不同才加进去
for i in range(len(data_blocks)):
    if data_blocks[i] not in blocks:#
        blocks.append(data_blocks[i])
for block_no in range(len(blocks)):#遍历data_blocks中不同的堆场号，每次不同时新加一个sheet页用来区分不同堆场
    # #添加Sheet页
    new_sheet = new_workbook.add_sheet(blocks[block_no])#此时不允许对单元格内容进行覆盖，若需要覆盖需要使用cell_overwrite_ok=True

    #设置sheet页第一行数据，用来显示堆场贝位，1/3/5/7.。。将第一行数据填入贝位号
    for field in range(150):
        if field%2 !=0:
            #此时都是奇数，将sheet页第一行数据写入贝位号
            new_sheet.write(0,int((field+1)/2),field)

    #设置sheet页第一列数据，用来显示同一贝位不同列的不同层，将5层合并作为一个列
    for lane in range(11):#堆场列的值
        if lane!=0:
            #比如第一列=1列
            message = "{0}列(从上到下from1to5层)".format(lane)
            new_sheet.write_merge(1+5*(lane-1),5+5*(lane-1),0,0,message)#write_merge(a,b,c,d,message)函数将从第a行到第b行的第c列到第d列的单元格合并，并填入内容message

    #设置单元格填充颜色style
    style_20 = xlwt.easyxf('pattern:pattern solid, fore_colour red;')#20尺箱子要填入的颜色
    style_40 = xlwt.easyxf('pattern:pattern solid, fore_colour green;')#40尺箱子要填入的颜色
    style_45 = xlwt.easyxf('pattern:pattern solid, fore_colour orange;')#45尺箱子要填入的颜色

    #开始写入数据
    for i in range(len(data_bays)):#遍历有多少个箱子
        try:
            if blocks[block_no]==data_blocks[i]:
                if data_bays[i]%2==0:#偶数，表示是40尺/45尺箱子
                    #此时需要填充2个单元格，因为40尺占用了2个单20尺的位置
                    row_index = data_tiers[i]+5*(data_lanes[i]-1)
                    col_index1 = int(data_bays[i]/2)
                    col_index2 = int(col_index1+1)
                    # print("data_bays[i]={0},data_lanes[i]={1},data_tiers[i]={2},row_index={3},col_index1={4},col_index2={5}".format(data_bays[i],data_lanes[i],
                    #                                                                                                                 data_tiers[i],row_index,col_index1,col_index2))
                    if data_containerids[i]=='':#说明此时无箱号信息
                        #40尺箱子加入到单元格中
                        new_sheet.write_merge(row_index,row_index,col_index1,col_index2,'40尺',style_40)#write_merge(a,b,c,d,message)函数将从第a行到第b行的第c列到第d列的单元格合并，并填入内容message
                    else:
                        # 说明此时有箱号信息
                        # 40尺箱子加入到单元格中
                        new_sheet.write_merge(row_index, row_index, col_index1, col_index2, data_containerids[i],style_40)  # write_merge(a,b,c,d,message)函数将从第a行到第b行的第c列到第d列的单元格合并，并填入内容message
                else:#奇数,表示是20尺箱子，贝列层数据不需要处理
                    row_index = data_tiers[i] + 5 * (data_lanes[i] - 1)
                    col_index = int((data_bays[i]+1)/2)
                    if data_containerids[i]=='':#说明此时无箱号信息
                        new_sheet.write(row_index, col_index,'20尺',style_20)
                    else:#说明此时有箱号信息
                        new_sheet.write(row_index, col_index, data_containerids[i],style_20)
        except:
            print("未知异常！存在相同的贝列层,可能40尺和20尺位置覆盖了！")
            print("data_blocks[i]={3},data_bays[i]={0},data_lanes[i]={1},data_tiers[i]={2}".format(data_bays[i],data_lanes[i],data_tiers[i],data_blocks[i]))
        else:
            continue

# 保存文件
new_workbook.save(target_file)



