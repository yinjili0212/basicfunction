# -*- coding: utf-8 -*-

import socket
import re
import os
import threading
import urllib.parse


def service_client(new_socket):
    # 为这个客户端返回数据
    # 1.接收浏览器发过来的请求，即http请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode('utf-8')
    request_header_lines = request.splitlines()
    print(request_header_lines)
    data = request_header_lines[-1]
    # ret = re.match(r'[^/]+(/[^ ]*)', request_header_lines[0])
    ret = list(request_header_lines[0].split(' '))[1]
    method = list(request_header_lines[0].split(' '))[0]
    path_name = "/"

    if method == 'GET':
        if ret:
            path = ret
            path_name = urllib.parse.unquote(path)  # 浏览器请求的路径中带有中文，会被自动编码，需要先解码成中文，才能找到后台中对应的html文件
            print("请求路径：{}".format(path_name))

        if path_name == "/":  # 用户请求/时，返回咖啡.html页面
            path_name = "/咖啡.html"

        # 2.返回http格式的数据给浏览器
        file_name = 'E:/pythonProject2/httpweb/HTML/' + path_name
        try:
            f = open(file_name, 'rb')
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n"
            response += "\r\n"
            response += "------file not found------"
            new_socket.send(response.encode("utf-8"))
        else:
            html_content = f.read()
            f.close()
            # 准备发给浏览器的数据 -- header
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            new_socket.send(response.encode("utf-8"))
            new_socket.send(html_content)
            # 关闭套接字
    if method == 'POST':
        if ret:
            path = ret
            path_name = urllib.parse.unquote(path)  # 浏览器请求的路径中带有中文，会被自动编码，需要先解码成中文，才能找到后台中对应的html文件
            print("请求路径：{}".format(path_name))
        if path_name == "/":  # 用户请求/时，返回咖啡.html页面
            path_name = "/咖啡.html"

        # 2.返回http格式的数据给浏览器
        file_name = 'E:/pythonProject2/httpweb/HTML/' + path_name
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(file_name.encode("utf-8") + '    data:'.encode("utf-8") + data.encode("utf-8"))
    if method == 'PUT':
        if ret:
            path = ret
            path_name = urllib.parse.unquote(path)  # 浏览器请求的路径中带有中文，会被自动编码，需要先解码成中文，才能找到后台中对应的html文件
            print("请求路径：{}".format(path_name))
        if path_name == "/":  # 用户请求/时，返回咖啡.html页面
            path_name = "/咖啡.html"

        # 2.返回http格式的数据给浏览器
        file_name = list(request_header_lines[0].split(' '))[1] + 'test.txt'
        content = data.encode('utf-8')
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        with open(file_name, 'ab') as f:
            f.write(content)
        new_socket.send(response.encode("utf-8"))
        new_socket.send("finish".encode("utf-8"))
    if method == 'HEAD':
        if ret:
            path = ret
            path_name = urllib.parse.unquote(path)
            print("请求路径:{}".format(path_name))
        if path_name == "/":
            path_name = "/咖啡.html"
        response = "HTTP/1.1 200 ok\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(str(request_header_lines[1:]).encode("utf-8"))
    if method == 'OPTION':
        if ret:
            path = ret
            path_name = urllib.parse.unquote(path)
            print("请求路径:{}".format(path_name))
        if path_name == "/":
            path_name = "/咖啡.html"
        response = "HTTP/1.1 200 ok\r\n"
        new_socket.send(response.encode("utf-8"))
        new_socket.send("OPTION,GET,HEAD,POST,PUT,DELETE".encode("utf-8"))
    if method == 'DELETE':
        if ret:
            path = ret
            path_name = urllib.parse.unquote(path)  # 浏览器请求的路径中带有中文，会被自动编码，需要先解码成中文，才能找到后台中对应的html文件
            print("请求路径：{}".format(path_name))
        if path_name == "/":  # 用户请求/时，返回咖啡.html页面
            path_name = "/咖啡.html"

        deletename = request_header_lines[-1]
        # print(path_name+deletename)
        os.remove(path_name + deletename)
        # 2.返回http格式的数据给浏览器
        content = data.encode('utf-8')
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # with open(file_name, 'ab') as f:
        #     f.write(content)
        new_socket.send(response.encode("utf-8"))
        new_socket.send("finish".encode("utf-8"))
    # 关闭套接字
    new_socket.close()


def main():
    # 用来完成整体的控制
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定
    tcp_server_socket.bind(("127.0.0.1", 8100))
    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        try:
            # 4.等待新客户端的链接
            new_socket, client_addr = tcp_server_socket.accept()
            # 5.为这个客户端服务
            print("为", client_addr, "服务")
            t = threading.Thread(target=service_client, args=(new_socket,))
            t.start()
            #
            # # 关闭监听套接字
            # tcp_server_socket.close()
        except:
            continue

if __name__ == '__main__':
    main()