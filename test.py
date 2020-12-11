# coding=utf-8
import sys
# reload(sys)
from flask import Flask, request
import flask_restful
from flask_restful import Resource

app = Flask(__name__)
api = flask_restful.Api(app)

user_pwd = {'admin': '123456'}


class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}


class TodoSimple(Resource):
    def get(self):
        return {'1': '123'}

    def put(self):
        params = request.json
        print(params)
        # 参数为json
        user = params.get('user')
        # user = request.form['user']
        # 参数为原始格式
        if user in user_pwd.keys():
            return {'errorCode': '0',
                    user: user_pwd[user]}
        else:
            return {'errorCode': '1',
                    '': ''}


api.add_resource(HelloWorld, '/')
# api.add_resource(TodoSimple, '/<string:todo_id>')
api.add_resource(TodoSimple, '/TodoSimple')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
