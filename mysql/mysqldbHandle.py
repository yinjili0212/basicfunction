import mysql.connector

import pandas as pd

# 注：设置环境编码方式，可解决读取数据库乱码问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
pd.set_option('display.width', 5000)
class MysqldbHandler:
    def __init__(self,host,user,password,database):
        #连接数据库
        self.conn = mysql.connector.connect(host=host,  user=user,  password=password,  database=database)
        #创建游标
        self.cur = self.conn.cursor()

        # 实现查询并返回 o返回原始数据，df返回dataFrame表格,d返回dict(默认)

    def query(self, sql, t='d', source=False):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        col = [col[0] for col in self.cur.description]
        if len(result) == 0:
            return []
        else:
            if t == 'o':
                return result
            elif t == 'df':
                results = pd.DataFrame(result)
                results.columns = col
                if source:
                    return results, result
                else:
                    return results
            elif t == 'd':
                rd = []
                for r in result:
                    rd.append({col[n]: r[n] for n in range(len(r))})
                return rd

    def getData(self, table, fields, conditions=None):
        if conditions:
            sql = "select " + fields + " from " + table + " where " + conditions + ""
        else:
            sql = "select " + fields + " from " + table
        self.cur.execute(sql)
        result = self.cur.fetchall()
        col = [col[0] for col in self.cur.description]
        rd = []
        for r in result:
            rd.append({col[n]: r[n] for n in range(len(r))})
        return rd

    def first(self, rd):
        if rd:
            return rd[0]
        else:
            return {}

    def delData(self, table, conditions=None):
        if conditions:
            sql = "delete from " + table + " where " + conditions + ""
        else:
            sql = "delete from " + table
        self.cur.execute(sql)
        self.conn.commit()

        # 执行sql并commit

    def executesql(self, sql):
        self.cur.execute(sql)
        self.conn.commit()


    def close(self):
        self.cur.close()
        self.conn.close()
