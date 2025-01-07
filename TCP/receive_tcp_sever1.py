import socket
#TCPserver端必须开启状态，client端才能发送，否则会报错
#参考网址：https://blog.csdn.net/weixin_66398100/article/details/128958023
def main():
    # 1.创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #  2.必须选择接收时的ip和端口 (ip,端口)
    tcp_server_socket.bind(('127.0.0.1', 7777))

    # 3.监听将tcp的主动连接特性转为被动连接，最大可支持128个客户端的连接
    tcp_server_socket.listen(128)

    while True:
        # 4.等待接收（accept）客户端的链接
        # 返回的是一个元组(一个新的tcp套接字对象，对方的ip和端口)
        new_client_socket, client_addr = tcp_server_socket.accept()
        print('当前客户端是: %s' % str(client_addr))

        # 5.接收对方发送的数据
        while True:
            recv_data = new_client_socket.recv(1024).decode('utf-8')
            print('当前客户端地址：{}，当前接受的信息是：{}'.format(client_addr[0], recv_data))

if __name__ == '__main__':
    main()

