import sqliteHandle
o=sqliteHandle.sqliteHandler('example.db')
a=o.query("select * from stocks")
b =o.getData("stocks",'*')
o.delData("stocks","symbol='RHAT'")
print(b)
