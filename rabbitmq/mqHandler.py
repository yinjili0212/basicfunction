import pika
import json
import uuid
import datetime
import yaml

class MqHandler:
    def __init__(self,env):
        self.env=env
        self.conf = yaml.full_load(open('../doc/config.yml', 'r', encoding='utf-8').read()).get(env).get('rabbitmq')
        self.channel,self.conn = self.iniConnMq()


    def iniConnMq(self):
        credentials = pika.PlainCredentials(self.conf.get('user'), self.conf.get('password'))  # mq用户名和密码
        # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
        connection = pika.BlockingConnection(pika.ConnectionParameters(host = self.conf.get('host'), port =  self.conf.get('port'),
                                                                       virtual_host = self.conf.get('virtual_host'), credentials = credentials))
        channel=connection.channel()
        # 声明消息队列，消息将在这个队列传递，如不存在，则创建
        channel.exchange_declare(exchange=self.conf.get('exchange'), exchange_type=self.conf.get('exchange_type'))
        return channel,connection

    def sendMqMsg(self,msg,routing_key,exchange):#注意rabbitmq中经常用的3个不同的exchange，需要名字对应
        msg_props = pika.BasicProperties()
        msg_props.content_type = "application/json"
        jmsg = json.dumps(msg)
        self.channel.basic_publish(
            exchange=exchange, routing_key=routing_key, body=jmsg,properties=msg_props)
    def startConsume(self,queue,cbfunc,routing_key):
        # 创建临时队列，队列名传空字符，consumer关闭后，队列自动删除
        result = self.channel.queue_declare(queue, exclusive=True)
        # 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
        self.channel.exchange_declare(exchange=self.conf.get('exchange'), durable=False, exchange_type='direct')
        # 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
        self.channel.queue_bind(exchange=self.conf.get('exchange'), queue=queue, routing_key=routing_key)

        # channel.basic_qos(prefetch_count=1)
        # 告诉rabbitmq，用callback来接受消息
        self.channel.basic_consume(result.method.queue, cbfunc,
                              # 设置成 False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
                              auto_ack=False)
        self.channel.start_consuming()

    def close(self):
        self.conn.close()

