from flask import Flask
from flask import request

# 配置对象
class DefaultConfig(object):
    CONFIG_KEY = 'wudnmjwsjj17djmsdji'

# 创建Flask项目的工厂函数
def create_flask_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app

# flask 类接收一个参数__name__
# app = Flask(__name__, static_folder='static', template_folder='templates', static_url_path='/s')
# 创建项目
app = create_flask_app(DefaultConfig)


# 从配置对象中加载配置信息 会覆盖掉从配置对象中加载的同名参数
# app.config.from_object(DefaultConfig)
# 从配置文件中加载配置信息
app.config.from_pyfile('config.py', silent=True)


# 装饰器的作用是将路由映射到视图函数index
@app.route('/')    # 访问路径
def index():       # 视图函数
    print("CONFIG_KEY: " + app.config['CONFIG_KEY'])
    return 'Hello! Web App with Python Flask!'



# a simple page that says hello
@app.route('/hello')
def hello():
    print("CONFIG_KEY: " + app.config['CONFIG_KEY'])
    return 'Hello, World!'

@app.route('/name', methods=['GET', 'POST'])
def get_name():
    if request.method == 'POST':
        # name
        # fans
        print(request.json)
        name = request.json.get('name')
        fans = request.json.get('fans')
        # 获取post body中的name和fans
        return 'Mesg from POST ' + 'Name: ' + name + ' fans: ' + fans
    else:
        return 'Mesg from GET'


# flask应用程序实例的run方法启动web服务器
# app.run(host='0.0.0.0', port=81)
# flask 1.0 版本以后 不需要通过运行 app.run()来启动
# 具体方法 设置环境变量 export FLASK_APP=helloworld 然后 flask run
# 设置debug export FLASK_ENV=development
# if __name__ == '__main__':
#     app.run()  # Flask应用程序的run方法启动web服务器
