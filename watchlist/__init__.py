# -*- coding:utf-8 -*-

"""
@Author:    Browser
@file:      __init__.py 
@time:      2019/06/19
@contact:   browser_hot@163.com
@software:  PyCharm 
"""

import os
import sys
from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

# 程序对象
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
# 注意更新这里的路径，把 app.root_path 添加到 os.path.dirname() 中,以便把文件定位到项目根目录
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path),os.getenv('DATABASE_FILE','data.db')) # 数据库连接地址
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)
# 实例化扩展类
login_manager = LoginManager(app)
# 登入视图端点
login_manager.login_view = 'login'
# 未登入告警
login_manager.login_message = '请先登入'


@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数
    from watchlist.models import User
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象

# 模板上下文处理 user变量
@app.context_processor
def inject_user():  # 函数名可以随意修改
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)  # 需要返回字典，等同于return {'user': user}

# 为了避免循环依赖（A 导入 B，B 导入 A），我们把这一行导入语句放到构造文件的结尾
from watchlist import views,errors,commands
