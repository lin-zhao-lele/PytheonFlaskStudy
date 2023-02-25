from flask import Flask

# flask 类接收一个参数__name__
app = Flask(__name__)

# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return 'Hello! Web App with Python Flask!'

# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'

# flask应用程序实例的run方法启动web服务器
# app.run(host='0.0.0.0', port=81)
if __name__ == '__main__':
    app.run()