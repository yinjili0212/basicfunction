from flask import Flask
from flask_restful import Resource, Api
#参考网址：https://www.php.cn/faq/561094.html
app = Flask(__name__)
api = Api(app)
class Student(Resource):
    def get(self, id):
        # 获取指定id的学生信息
        pass

    def post(self):
        # 新增一个学生
        pass

    def put(self, id):
        # 更新指定id的学生信息
        pass

    def delete(self, id):
        # 删除指定id的学生信息
        pass

api.add_resource(Student, '/students', '/students/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)