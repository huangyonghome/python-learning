# -*- coding: utf-8 -*-
# @Time    : 2020-09-24 22:29
# @Author  : jesse
# @File    : hello.py

from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql://root:Iamyourdaddy@172.16.20.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)

    def __repr__(self):
        return '<Role %r>' %self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)

    def __repr__(self):
        return '<User %r>' %self.username

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

class NameForm(FlaskForm):
    name = StringField("what is your name?",validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET','post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False

        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',form=form,
                           name=session.get('name'),
                           known=session.get('known',False))