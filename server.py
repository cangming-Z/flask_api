# 通过flask框架搭建后台
import configparser
from os import path

from flask import Flask, request
from Utility import main_path
from Utility.db_helper import Database
from Utility.logger import Logger
from selenium import webdriver
from flask import render_template
# 解决ajax请求的跨域问题
from flask_cors import CORS

# 创建一个服务器对象
app = Flask(__name__)
log = Logger(logger="test_main").get_log()

CORS(app, supports_credentials=True)


# 设置处理请求的功能(路由route => 接口)

# 设置一个主页路由, 对应一个处理主页的功能方法, 返回主页信息
@app.route('/')
def home_action():
    return render_template('测试ajax.html')


# 为ajax登录请求配置一个处理登录的功能
@app.route('/login')
def login_action():
    # 拿到前台数据, 进一步判断处理
    # 需要: 需要账号与密码, 匹配成功与否决定返回结果
    user = request.args['user']  # 'user'是规定前台需要传入数据的key
    pwd = request.args['pwd']
    # print(user)
    if user == 'abc' and pwd == '123':

        # 获取项目根目录
        filepath = main_path.get_obj_path()
        config = configparser.ConfigParser()
        filePath = path.sep.join([filepath, 'config', 'db.ini'])
        config.read(filePath, encoding='utf-8')

        project = 'WebAutoTest'

        host = config[project]["host"]
        port = eval(config[project]["port"])
        user = config[project]["user"]
        passwd = config[project]["passwd"]
        db = config[project]["db"]
        charset = config[project]["charset"]

        mysql_db = Database(host, port, user, passwd, db, charset)
        mysql_db.get_mysql_con_cursor()

        sql_process = 'select * from custom_process where project_id = %s and process_id = %s ' % (1, 1)

        sql_process_detail = 'select type,elements_msg,value from custom_process_detail ' \
                             'where project_id = %s and process_id = %s order by `index`' \
                             % (1, 1)
        process_detail = mysql_db.db_rw(sql_process_detail)

        option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=option)
        # browser = webdriver.Firefox()
        # 设置浏览器最大加载时间
        driver.set_page_load_timeout(8)
        err_msg = None

        for detail in process_detail:
            try:
                return_message = ''
                if detail[0] == '1':
                    return_message = driver.get(detail[2])
                elif detail[0] == '2':
                    return_message = driver.find_element_by_id(detail[1]).send_keys(detail[2])
                elif detail[0] == '3':
                    return_message = driver.find_element_by_class_name(detail[1]).click()
            except Exception as e:
                log.error(e)
                err_msg = "%s出错，错误信息：%s" % (detail[0], e)

        if err_msg is None:
            log.info('测试通过')
            return "登录成功，测试通过"
    return "登录失败"


# 启动服务(该文件作为自启文件)
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(port="8888")