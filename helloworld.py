#!/usr/bin/env python3

from flask import Flask, render_template
from markupsafe import Markup
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
	titleText="Hello Title"
	bodyText="Hello World"
	bodyText=bodyText + Markup("""
	Welcome to Flask
	<br>
	 <a href=/aggie>Say Hi to an Aggie</a>
	 <a href=/randomNumber>Create a random Number</a>
	 <a href=/time>Look at the time</a>
	 <a href=/about>Learn more about me
	</br>""")
	return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/time')
def time():
	titleText ="Current time"
	bodyText = "This is the current time: " + str(datetime.now().strftime("%I:%M:%S %p"))
	bodyText = bodyText +  Markup("""
	<br>
	 <a href=/>home</a>
	</br>""")
	return render_template('template.html', titleText=titleText, bodyText = bodyText)

@app.route('/about')
def about():
	titleText="Aboout Us"
	bodyText = "Hello this is Cade La Turner and I am doing this through Flask"
	bodyText =bodyText +  Markup("""
	<br>
	 <a href=/>home</a>
	</br>""")
	return render_template('template.html', titleText = titleText, bodyText = bodyText)

@app.route('/aggie')
def aggie():
	titleText="Hello Aggie"
	bodyText=Markup("""
	You have reached an aggie
	<br>
	 <a href=/>home</a>
	</br>""")
	return render_template('template.html',titleText=titleText, bodyText=bodyText)

@app.route('/randomNumber')
def randomNumber():
	titleText="A Random Number"
	bodyText="Your Random Number is " + str(random.randint(0,10000))
	bodyText=bodyText + Markup("""
	<br>
	 <a href=/>home</a>
	</br>""")
	return render_template('template.html', titleText=titleText, bodyText=bodyText)


if __name__== '__main__':
	app.run(host='0.0.0.0', debug = True)
