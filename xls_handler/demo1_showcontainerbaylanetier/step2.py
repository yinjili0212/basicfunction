import xlrd
import xlwt

#将上一步得到的sheet页为源头数据进行数据提取，将bay信息写入第1列，lane写入第2列，tier写入第三列，箱号写入第4列，堆场号写入第5列
#读取数据
old_book= xlrd.open_workbook(r'./block_container_show2.xls')


#打开sheet页
old_sheet = old_book.sheet_by_name("init_datas")


#需要写入的文件
new_book = xlwt.Workbook()
#打开sheet页
new_sheet = new_book.add_sheet('datasource',cell_overwrite_ok=True)#允许内容覆盖

#读取源头数据
first_col_values = old_sheet.col_values(colx=0,start_rowx=0,end_rowx=None)
second_col_values = old_sheet.col_values(colx=1,start_rowx=0,end_rowx=None)
for row_index in range(len(first_col_values)):
    container_wiref = first_col_values[row_index]
    block_no = second_col_values[row_index][5:7]
    bay_no = second_col_values[row_index][8:11]
    lane_no = second_col_values[row_index][12:14]
    tier_no = second_col_values[row_index][15:]
    #对数据进行分析后写入新sheet页
    new_sheet.write(row_index,0,bay_no)
    new_sheet.write(row_index, 1, lane_no)
    new_sheet.write(row_index, 2, tier_no)
    new_sheet.write(row_index, 3, container_wiref)
    new_sheet.write(row_index, 4, block_no)

#写入第一行数据
new_sheet.write(0,0,'bay')
new_sheet.write(0,1,'lane')
new_sheet.write(0,2,'tier')
new_sheet.write(0,3,'container')
new_sheet.write(0,4,'block_no')
new_book.save(r'./block_container_show3.xls')