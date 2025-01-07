import redis


class RedisHandler():

    def __init__(self,host,port,db,password):
        self.rds = redis.Redis(host,port,db,password,decode_responses=True)

    #删除list
    def delRdsList(self,name):
        #start > end 就是删除所有
        self.rds.ltrim(name,1,0)

    #删除所有name
    def delRdsLike(self,name):
        ks = self.rds.keys(name)
        for k in ks:
            self.rds.delete(k)

    #查询set
    def querySet(self,name):
        return self.rds.smembers(name)

    def addSet(self,name,value):
        self.rds.sadd(name,value)
    #查询hash
    def queryHash(self,name):
        return self.rds.hgetall(name)

    #redis.rpush('list', 1, 2, 3) 添加值到name
    def addList(self,name,*value):
        self.rds.rpush(name,*value)

    #返回list所有元素
    def getList(self,name):
        return self.rds.lrange(name,0,self.rds.llen(name)-1)

    def set(self,name,value):
        self.rds.set(name,value)

    def get(self,name):
        return self.rds.get(name)

    def delete(self,name):
        self.rds.delete(name)

    def flushdb(self):
        self.rds.flushdb()

    def close(self):
        self.rds.close()
