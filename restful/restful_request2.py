import requests
import json

#参考网址：https://www.php.cn/faq/561094.html

# # 新增一个学生
# data = {
#     "name": "Tom",
#     "age": 20,
#     "gender": "Male"
# }
# headers = {
#     "content-type": "application/json"
# }
# # response = requests.post("http://localhost:5000/students", data=json.dumps(data), headers=headers)
# # print(response.content)

# # 获取指定id的学生信息
# response = requests.get("http://localhost:5000/students/1")
# print(response.content)
## 获取指定id的学生信息
response = requests.get("http://10.128.231.182:31082/")
print(response.content)
# # 更新指定id的学生信息
# data = {
#     "name": "Tom",
#     "age": 21,
#     "gender": "Male"
# }
# headers = {
#     "content-type": "application/json"
# }
# response = requests.put("http://localhost:5000/students/1", data=json.dumps(data), headers=headers)
# print(response.content)
#
# # 删除指定id的学生信息
# response = requests.delete("http://localhost:5000/students/1")
# print(response.content)