import pika
import datetime
import time
#参考网址：https://pythonjishu.com/blgwieeoiqbegnr/
####################################################################################################################读取rabbitmq
USERNAME = 'admin' # 用户名
PASSWROD = 'Zpmc@254.34' # 密码
HOST = '10.128.254.34' # rabbitMQ的IP
PORT = 5672 # 端口
##direct类型的exchange
WRITE_QUEUE='demo_write.queuetopic' # 队列
# WRITE_EXCHANGE='demo.exchangedirect' # 交换机
# ROUTING_KEY='demodirect' # routing-key
credentials = pika.PlainCredentials(username=USERNAME, password=PASSWROD)
connection = pika.ConnectionParameters(host=HOST, port=PORT, credentials=credentials)
# # 这个方式最简单了，当程序启动后会进行阻塞，当有消息来的时候就会进行消费，消费完成后在尝试获取下一个
channel = pika.BlockingConnection(connection).channel()

# 回调处理函数
# 此时需要准备一个回调函数，参数不过多解释
def call_back(ch, method, properties, body):
    # 获取一条消息（如果直接获取会是乱码）
    message = str(body.decode('utf-8'))

    # 处理逻辑
    print(message)

    # ack确认(确定接收成功后调用，不然消息会一直存在)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# # 告诉rabbitmq，用callback来接受消息
channel.basic_consume(WRITE_QUEUE, call_back,
                           # 设置成 False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
                           auto_ack=False)
channel.start_consuming()