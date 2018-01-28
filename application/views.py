# coding:utf-8
from application import app
from flask import request, render_template, redirect, url_for, session, make_response, abort


@app.route('/')
@app.route('/index')
def home():
    return render_template('pc/home.html')


@app.route('/jobs')
def jobs():
    return render_template('pc/jobs.html')


@app.route('/summary')
def summary():
    return render_template('pc/summary.html')


@app.route('/about')
def about():
    return render_template('pc/about.html')
