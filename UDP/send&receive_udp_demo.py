import socket
#####################################################################发送UDP数据
#参考网址：https://zhuanlan.zhihu.com/p/565478180
#设置要绑定的IP地址和端口号
ip = '127.0.0.1'
port = 8080
# 创建Socket对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.AF_INET（是ip4还是ip6-是固定的） socket.SOCK_STREAM（使用udp也是固定的）

# 设置要绑定的IP地址和端口号
udp_socket.bind((ip, port))

# 设置要发送的数据
data = "Hello, World!".encode('utf-8')#使用encode编码，使用decode解码decode('utf-8')
# 使用socket发送数据
udp_socket.sendto(data, (ip, port))
# 关闭socket连接
udp_socket.close()

#####################################################################接收UDP数据
#接收时，设置循环运行程序且socket对象不能关闭，参考circle_send&receive.py
#设置要绑定的IP地址和端口号
ip = '127.0.0.1'
port = 8080
# 创建Socket对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.AF_INET（是ip4还是ip6-是固定的） socket.SOCK_STREAM（使用udp也是固定的）

# 设置要绑定的IP地址和端口号
udp_socket.bind((ip, port))

# 设置接收数据的缓存区大小
buf_size = 1024

# 接收数据
recv_data = udp_socket.recvfrom(buf_size)
# 输出接收到的数据
recv_msg = recv_data[0].decode('utf-8')  # 储存接收的数据并且解码
send_addr = recv_data[1]  # 储存发送的地址信息

print(f"{send_addr}{recv_msg}")
# 关闭Socket对象
udp_socket.close()
