from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from flask import render_template, redirect, request, session
from app import app, db
from .models import Markov
from .bots import Bot
from .chat import getReply
import sys

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/frondz', methods=['GET', 'POST'])
def frondz_app():
    if 'chatHistory' not in session:
        session['chatHistory'] = []
    if 'bots' not in session:
        session['bots'] = [ u"FritzBot", u"NomeBot" ]
    form = ChatForm()
    if request.method == 'POST':
        text = form.msg.data
        if text == u"reset!!!":
            session.clear()
            return redirect('/frondz')
        name = 'You'
        session['chatHistory'].append({'name' : name, 'text' : text})
        for bot in session['bots']:
            session['chatHistory'].append({'name' : bot, 'text' : getReply(bot, text)})
        return redirect('/frondz')
    return render_template('frondz.html', form=form, chats=getLastChats(9))
    
class ChatForm(Form):
    msg = StringField('msg')
    send = SubmitField('send')
    
def getLastChats(num):
    if len(session['chatHistory']) > num * 2:
        session['chatHistory'] = session['chatHistory'][-(num * 2):]
    if len(session['chatHistory']) > num:
        return session['chatHistory'][-(num):]
    else:
        return session['chatHistory']
        