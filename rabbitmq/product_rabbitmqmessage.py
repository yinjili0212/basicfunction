import pika
import json
import time
import datetime
#参考网址：https://pythonjishu.com/blgwieeoiqbegnr/
###################################################################################################################写入rabbitmq
while True:
    msg=[{"AHT_ID":"V003","QC_ID":"QC101"}]
    def msgTqmiHandle(msg):

        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


        message={"HEAD": {"TIME_ID":t,"EVENT_SUB_TYPE": 'EVENT_SUB_TYPE',"USER_CODE": "LINWT",
                          "APP_ID": "FOURTIER_SERVER","FACILITY_ID": "NUCT","EVENT_TYPE": 'EVENT_TYPE',
                          "EVENT_ID": "6f2ed3bb-e6da-444c-bd02-3dfd06162bda"},"BODY": []}
        if isinstance(msg,list):
            message['BODY']= msg
        else:
            message['BODY']=[msg]
        return message

    USERNAME = 'admin' # 用户名
    PASSWROD = 'Zpmc@254.34' # 密码
    HOST = '10.128.254.34' # rabbitMQ的IP
    PORT = 5672 # 端口
    ##direct类型的exchange
    # WRITE_QUEUE='demo_write.queuedirect' # 队列
    # WRITE_EXCHANGE='demo.exchangedirect' # 交换机
    # ROUTING_KEY='demodirect' # routing-key

    # ##fanout类型的exchange
    # WRITE_QUEUE='demo_write.queuefanout' # 队列
    # WRITE_EXCHANGE='demo.exchangefanout' # 交换机
    # ROUTING_KEY='demofanout' # routing-key

    ##topic类型的exchange
    WRITE_QUEUE='demo_write.queuetopic' # 队列
    WRITE_EXCHANGE='demo.exchangetopic' # 交换机
    ROUTING_KEY='demotopic' # routing-key

    # 创建一个凭证
    credentials=pika.PlainCredentials(username=USERNAME,password=PASSWROD)
    # 创建一个连接
    connection = pika.ConnectionParameters(host=HOST,port=PORT,credentials=credentials)
    # 建立连接并获取一个通道，
    # 此处采用阻塞连接（这个方式最简单了，但是对于生产者没啥区别）
    channel = pika.BlockingConnection(connection).channel()
    # 创建交换机和队列，如果没有就会自动创建
    # 如果已经创建的与当前定义的不一样会**报错**
    # 此处durable表示是是否持久化，exchange_type对应exchange不同类型
    # channel.exchange_declare(exchange=WRITE_EXCHANGE,durable=True,exchange_type='direct')
    # channel.exchange_declare(exchange=WRITE_EXCHANGE,durable=True,exchange_type='fanout')
    channel.exchange_declare(exchange=WRITE_EXCHANGE,durable=True,exchange_type='topic')
    channel.queue_declare(queue=WRITE_QUEUE,durable=True)
    # 绑定
    # 如果队列或交换机不存在**报错**
    channel.queue_bind(queue=WRITE_QUEUE,exchange=WRITE_EXCHANGE,routing_key=ROUTING_KEY)
    message = msgTqmiHandle(msg)

    #设置消息格式为json
    msg_props = pika.BasicProperties()
    msg_props.content_type = "application/json"#定义消息属性
    jmsg = json.dumps(message)
    print(message)
    # # 进行生产
    channel.basic_publish(exchange=WRITE_EXCHANGE,routing_key=ROUTING_KEY,body=jmsg,properties=msg_props)
    time.sleep(3)