# coding=utf-8
import http.client
from urllib import request, parse


def send_get(url, path, data):  # get请求函数
    conn = http.client.HTTPConnection(url)
    conn.request("GET", path)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()
    print(data1)  #
    conn.close()


def send_post(url, path, data, header):  # post请求函数
    conn = http.client.HTTPConnection(url)  # 建立连接
    conn.request("POST", path, data, header)  # 用request请求，将信息封装成帧
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()
    print(data1)  #
    conn.close()


def send_head(url, path, data, header):
    conn = http.client.HTTPConnection(url)
    conn.request("HEAD", path, data, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.headers  #
    print(data1)  #
    conn.close()


def send_put(url, path, filedata, header):
    conn = http.client.HTTPConnection(url)
    conn.request("PUT", path, filedata, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()  #
    print(data1)
    conn.close()


def send_option(url, path, data, header):
    conn = http.client.HTTPConnection(url)
    conn.request("OPTION", path, data, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.headers  #
    print(data1)  #
    conn.close()


def delete_option(url, path, filename, header):
    conn = http.client.HTTPConnection(url)
    conn.request("DELETE", path, filename, header)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)

    data1 = r1.read()  #
    print(data1)
    conn.close()


if __name__ == '__main__':

    url = "127.0.0.1:8100"
    data = {
        'my post data': 'I am client , hello world',
    }
    datas = parse.urlencode(data).encode('utf-8')
    print(datas)

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    while True:
        try:
            command = input("输入请求的命令：")
            if command == 'get':
                print("----------发送get请求:-----------")
                send_get(url, path="", data="None")
            elif command == 'post':
                print("----------发送post请求-----------")
                send_post(url, path="", data=datas, header=headers)

            elif command == 'put':
                print("----------发送put请求-----------")
                file = input("输入要发送的文件名:")
                tfile = open(file, encoding='UTF-8', mode='r')
                filedatas = tfile.read()
                fileheaders = {"Content-type": "text/plain", "Accept": "text/plain","content-length": str(len(filedatas))}
                send_put(url, path="F:/OneDrive - shzpmc/python完整脚本/basicfunction/HTTP/", filedata=filedatas, header=fileheaders)
            elif command == 'head':
                print("----------发送head请求:-----------")
                send_head(url, path="", data=datas, header=headers)
            elif command == 'option':
                print("----------发送option请求:-----------")
                send_option(url, path="", data=datas, header=headers)
            elif command == 'delete':
                print("----------发送delete请求-----------")
                file = input("输入要删除的文件名:")
                fileheaders = {"Content-type": "text/plain", "Accept": "text/plain"}
                delete_option(url, path="E:/pythonProject2/httpweb/", filename=file, header=fileheaders)
            elif command == 'exit':
                break
        except:
            continue
