# -*- coding:utf-8 -*-

"""
@Author:    Browser
@file:      wsgi.py 
@time:      2019/06/19
@contact:   browser_hot@163.com
@software:  PyCharm 
"""

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app