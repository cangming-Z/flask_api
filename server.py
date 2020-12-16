# 通过flask框架搭建后台

from flask import Flask, request

# 创建一个服务器对象
app = Flask(__name__)

# 解决ajax请求的跨域问题
from flask_cors import CORS

CORS(app, supports_credentials=True)


# 设置处理请求的功能(路由route => 接口)

# 设置一个主页路由, 对应一个处理主页的功能方法, 返回主页信息
@app.route('/')
def home_action():
    return '<h1 style="color: red">主页</h1>'


# 为ajax登录请求配置一个处理登录的功能
@app.route('/login')
def login_action():
    # 拿到前台数据, 进一步判断处理
    # 需要: 需要账号与密码, 匹配成功与否决定返回结果
    user = request.args['user']  # 'user'是规定前台需要传入数据的key
    pwd = request.args['pwd']
    # print(user)
    if user == 'abc' and pwd == '123':
        return "登录成功"
    return "登录失败"


# 启动服务(该文件作为自启文件)
if __name__ == '__main__':
    app.run(port="8888")