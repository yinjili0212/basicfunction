import socket

#参考网址：https://zhuanlan.zhihu.com/p/565478180
def main():
    # 1、创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2、server端绑定端口号
    ip = '127.0.0.1'
    port = 7788
    udp_socket.bind((ip, port))
    # 3、循环来处理反复接收
    while True:
        # 1、发送信息并获取发送的信息。
        send_data = 'this is test data.'
        udp_socket.sendto(send_data.encode('utf-8'), (ip, port))
        # 2、接收并解析
        recv_date = udp_socket.recvfrom(1024)
        print(f"{recv_date[1]}{recv_date[0].decode('utf-8')}")



if __name__ == '__main__':
    main()