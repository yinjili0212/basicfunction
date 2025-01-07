import xlrd
import xlwt

#通过给出的xls提取关键信息，将箱号写入第一列，堆场信息写入第2列=YARD.CA.010.01.05
# ####################################################################################################################################读取xls数据函数
# url = r'./多ASC_RC1 112-116.xlsx'
# url = r'./多ASC_RC1班轮-qcdispatchnostowfactor.xlsx'

# url = r'./多ASC_RC1轻桥泊位(7-9泊位).xlsx'

# url = r'./多ASC_RC1轻桥泊位(11-12泊位).xlsx'
# url = r'./多ASC_RC1主泊位驳船.xlsx'
url = r'./多ASC-门机PC01-05.xlsx'
#打开指定的工作薄
workbook = xlrd.open_workbook(url)
###############获取工作表格的三种方法
## 获取工作表格的3种方法，第3种方法
old_sheet = workbook.sheet_by_name("WI")   #workbook.sheet_by_name(sheet名称)：此前提是知道表格中的sheet名称



#获取第一行的数据
datas_row0s = old_sheet.row_values(rowx=0,start_colx=0,end_colx=None)

#将要写入的文件
new_book = xlwt.Workbook()
#打开sheet页
new_sheet =  new_book.add_sheet('init_datas',cell_overwrite_ok=True)
new_sheet.write(0,0,'箱号信息')
new_sheet.write(0,1,'堆场位置信息')

for col_index in range(len(datas_row0s)):
    if 'CONTAINER_WI_REF' == datas_row0s[col_index] or 'ORIGIN_SLOT' == datas_row0s[col_index] or 'DESTINATION_SLOT' == datas_row0s[col_index]:
            #得到每一列的数据，遍历每一列的数据
            cols_values = old_sheet.col_values(colx=col_index,start_rowx=0,end_rowx=None)
            if cols_values[0]=='CONTAINER_WI_REF':#说明此时是箱号，将信息写入新sheet页的第一列
                for col_value_index in range(len(cols_values)):
                    new_sheet.write(col_value_index,0,cols_values[col_value_index])
            if cols_values[0] == 'ORIGIN_SLOT' or cols_values[0] == 'DESTINATION_SLOT':  # 说明此时是堆场位置，将信息写入新sheet页的第2列
                for col_value_index in range(len(cols_values)):
                    #只有当YARD在关键字中才写入
                    if 'YARD' in cols_values[col_value_index]:
                        new_sheet.write(col_value_index, 1, cols_values[col_value_index])
new_book.save(r'block_container_show2.xls')







