from voran import app
from flask import Flask, render_template, request, flash, redirect, url_for, session

appName = "Voran Playground"

@app.route("/")
def home():
	appName = "Voran Playground"	
	return render_template('home.html', title=appName)






if __name__ == "__main__":
	app.run(debug=True)
