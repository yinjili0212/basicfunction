import redis

#连接redis
r = redis.Redis(host='10.128.254.21',port=6379,db=3,password='Zpmc@254.21',decode_responses=True)
################################################################################################redis中一些通用函数
######查询
# print(r.exists('name'))#检查redis的name是否存在,存在返回1，不存在返回0
# print(r.keys('*'))#根据* ？等通配符匹配获取redis的name
# print(r.randomkey())#随机获取一个redis的name（不删除）
# print(r.type('test'))# 获取name对应值的类
######写入
# r.rename('name','test')#重命名,将name重置为test
# r.move('test',4)# 将redis的某个name移动到指定的db下,一般用不到
######删除
# r.flushdb(asynchronous=False)#清空当前db中的数据,默认是同步。若开启异步asynchronous=True，会新起一个线程进行清空操作，不阻塞主线程
# r.flushall(asynchronous=False)#清空所有db中的数据，默认是同步。异步同flushdb
# r.delete('name')#根据name删除redis中的任意数据类型
# r.expire('name',1)#为某个name的设置过期时间

################################################################################################redis中对string类型的操作
######对string类型的查询
# r.get('key1')#获取某个key的值
# r.mget("key1","key2")#批量获取
# r.strlen("key")#返回key对应值的字节长度（一个汉字3个字节）
######对string类型的写入
# r.set('key', 'value')#在Redis中设置值，默认不存在则创建，存在则修改,set(name, value, ex=None, px=None, nx=False, xx=False)
# r.mset({"key1":'value1', "key2":'value2'})#批量设置值
# #在name对应的值后面追加内容
# r.set("key","value")
# print(r.get("key"))    #输出:'value'
# r.append("key","one")
# print(r.get("key"))    #输出:'valueone'
#对string、hash、list、set、有序set类型的删除
# r.delete('key','key1','key2')

################################################################################################redis中对list类型的操作
# # ######对list类型的查询
# print(r.lrange("name",0,-1))#分片获取元素
# r.llen('name')#name列表长度
# print(r.lindex("name",1))#根据索引获取列表内元素
#####对list类型的写入
# r.lpush('name','元素5','元素5')#元素从list的左边添加，可以添加多个,无时创建，有时追加操作
# r.lpushx('name','元素1')#当name存在时，元素才能从list的左边加入
# r.rpush('name','元素右','元素左')#元素从list右边添加，可以添加多个，无时创建，有时追加操作
# r.rpushx('name','元素1')#当name存在时，元素才能从list的右边加入
# r.linsert("name","BEFORE","元素3","元素1.5")# 在name对应的列表的某一个值前或后插入一个新值#在列表内找到第一个"元素2"，在它前面插入"元素1.5"
# r.linsert("name","AFTER","元素3","元素5")# 在name对应的列表的某一个值前或后插入一个新值#在列表内找到第一个"元素2"，在它后面插入"元素5"
# r.lset("name",0,"abc")#对list中的某一个索引位置重新赋值
#####对list类型的删除
# r.lrem("name",0,"元素5")#删除name对应的list中的指定值
'''# 参数：

   name:  redis的name
   num:   num=0 删除列表中所有的指定值；
          num=2 从前到后，删除2个；
          num=-2 从后向前，删除2个
   value: 要删除的值
          '''
# print(r.lpop("name"))#移除列表的左侧第一个元素，返回值则是第一个元素
# r.ltrim("name",0,2)#移除列表内没有在该索引之内的值
# r.delete('name')#对string、hash、list、set、有序set类型的删除




################################################################################################redis中对hash类型的操作
##########对hash类型的查询
# print(r.hget("name","key"))#在name对应的hash中根据key获取value，#输出:'value'
# print(r.hgetall("name"))#获取name所有键值对
# print(r.hmget("name",["key1","key2"]))#在name对应的hash中批量获取键所对应的值#输出:['aa', 'bb']
# print(r.hlen("name"))#获取hash键值对的个数#输出：2
# print(r.hkeys("name"))#获取hash中所有key
# print(r.hvals("name"))#获取hash中所有value
# print(r.hexists("name","key100"))#检查name对应的hash是否存在,存在=True，不存在=False#输出：Ture
# print(r.hstrlen('name','test'))#返回name对应的hash中key=test对应的值的字节数
##########对hash类型的写入
# r.hset("name","test","value2")#name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
# print(r.hsetnx('name','key','1'))#name对应的hash中设置一个键值对（不存在，则创建，返回1；存在，不修改，返回0）
# print(r.hincrby("name",'key',amount=10))#与hash中key对应的值,key对应得值必须是可相加类型int，不存在则创建key=amount(amount为整数)#返回：10
# print(r.hincrbyfloat("name",'key',amount=10.2))#与hash中key对应的值,key对应得值必须是可相加类型float，不存在则创建key=amount(amount为float)#返回：10
##########对hash类型的删除
# print(r.hdel('name',1,'1'))#删除指定name对应的key所在的键值对，删除成功返回1，失败返回0#输出：1

################################################################################################redis中对set类型的操作
##########对set类型的查询
# print(r.scard("name"))#获取name对应的集合中的元素个数
# print(r.smembers('name'))#获取name对应的集合的所有成员
# print(r.sismember('name','aa'))#检查value是否是name对应的集合内的元素,是返回1，不是返回0
# print(r.scard('name'))#对name的set元素个数查询
# print(r.sinter(['name1','name2']))#查询集合name1和name2元素的交集

# #在第一个name对应的集合中且不在其他name对应的集合的元素集合
# r.sadd("name","aa","bb")
# r.sadd("name1","bb","cc")
# r.sadd("name2","bb","cc","dd")
# print(r.sdiff(["name","name1","name2"]))#输出:{'aa'}
##########对set类型的写入&修改
# r.sadd("name","ff")#给name对应的集合中添加元素（name不存在：创建，name存在：追加值）
# r.smove('name','name1','aa')#将某个元素aa从一个集合name中移动到另外一个集合name1
# print(r.spop('name'))#从集合的右侧移除一个元素，并将其返回
##########对set类型的删除
# r.delete('name')#对整个name的删除





