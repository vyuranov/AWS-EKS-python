# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import os
from flask import Flask, redirect, url_for, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def main():
    return redirect(url_for('login'))

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/api')
def api():
	return render_template('api.html')

@app.route('/about')
def service():
	return render_template('about.html')

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
