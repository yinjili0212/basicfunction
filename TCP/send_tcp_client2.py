import socket
import time
#参考网址：https://blog.csdn.net/weixin_66398100/article/details/128958023

def main():
    #  1.创建tcp套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.连接server端的IP才能发送消息
    tcp_client_socket.connect(('127.0.0.1', 7777))

    while True:
        # 3.发送数据到指定的电脑
        send_data = 'this is test data.'.encode('utf-8')
        tcp_client_socket.send(send_data)
        print("发送数据{0}".format(send_data))
        time.sleep(5)

if __name__ == '__main__':
    main()