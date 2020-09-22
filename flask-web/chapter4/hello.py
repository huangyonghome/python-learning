#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 下午10:02
# @Author  : jesse
# @File    : hello.py

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask import Flask,render_template,session,redirect,url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField("what is your name?",validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        print(type(session))
        print(session)
        print(session.items())
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))