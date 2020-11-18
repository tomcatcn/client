#! usr/bin python3
# -*- coding:utf-8 -*-

 ######################################################
#        > File Name: flask_client.py
#      > Author:
 #     > Mail:
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file

app = Flask(__name__)

@app.route('/index')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

@app.route('/<username>/info')
def info(username):
    #个人信息
    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):
    #修改个人信息
    return send_file('templates/change_info.html')

@app.route('/<username>/topic/release')
def topic_release(username):
    #发表博客
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):
    #个人博客列表
    return send_file('templates/list.html')

@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):
    #博客内容详情
    return send_file('templates/detail.html')

@app.route('/flask_test')
def flask_test():
    return send_file('templates/test_test.html')

@app.route('/<username>/photos')
def photos(username):
    # 相册列表
    return send_file('templates/photo.html')

@app.route('/<username>/photos/detail/<p_id>')
def photos_detail(username,p_id):
    # 相册具体内容
    return send_file('templates/photo_detail.html')


if __name__ == '__main__':
    app.run(debug=True)

