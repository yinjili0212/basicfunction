from socket import *

#参考网址：https://www.cnblogs.com/LXP-Never/p/9432210.html
# 处理客户端请求
def handle(connfd):
  request = connfd.recv(4096)   # 接收请求

  # 防止客户端断开request为空
  if not request:
    return
  request_line = request.splitlines()[0]    # 返回第一行   GET / HTTP/1.1
  info = request_line.decode().split(' ')[1]
  if info == '/':
    with open('index.html') as f:
      response = "HTTP/1.1 200 OK\r\n"            # 响应行
      response += "Content-Type:text/html\r\n"    # 响应头
      response += '\r\n'                          # 空行
      response += f.read()                        # 响应体
      print(response)
  else:
    response = "HTTP/1.1 404 Not Found\r\n"
    response += "Content-Type:text/html\r\n"
    response += '\r\n'
    response += "<h1>Sorry...</h1>"

  connfd.send(response.encode())    # 发送给浏览器

sockfd = socket()   # 搭建tcp网络
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('127.0.0.1',8000))       # 绑定地址
sockfd.listen(3)                    # 设置监听
while True:
  connfd,addr = sockfd.accept()     # 获取连接端和地址
  handle(connfd)      # 处理客户端请求
  print(addr)
#在浏览器输入地址：127.0.0.1:8000，可以看到python打印address！