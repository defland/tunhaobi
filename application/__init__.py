#coding:utf-8
from flask import Flask 

def create_app():  
    app=Flask(__name__,instance_relative_config=True,)  
    app.config.from_object('config')
    app.config.from_pyfile('config.py')

    return app  

app = create_app()


# 从视图引入路由
import application.views

