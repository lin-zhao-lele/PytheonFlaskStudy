# Flask(__name__) 的初始化参数还可以包括

-- static_url_path

-- static_fold

-- template_fold

# Flask将配置信息

保存在 app.config 属性中 app.config.get(name) 或者 app.config[name]

提供两种方法来设置config， app.config.from_pyfile app.config.from_object

# 运行方式
flask 1.0 版本以后 不需要通过运行 app.run()来启动

具体方法 设置环境变量 export FLASK_APP=helloworld 然后 flask run

在Pycharm里面需要设置 Configuration，增加环境变量 FLASK_APP=helloworld 并且选Module方式运行 命令 flask 参数 run


# 查询路由信息
flask routes

# gfh 