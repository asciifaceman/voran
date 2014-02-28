from voran import app
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask import Response
import subprocess, time

appName = "Voran Playground"

@app.route("/")
def home():
	appName = "Voran Playground"	
	return render_template('home.html', title=appName)


@app.route("/test")
def test():
	def inner():
		proc = subprocess.Popen(['ps', 'faux'], shell=True, stdout=subprocess.PIPE)

		for line in iter(proc.stdout.readline, ''):
			time.sleep(1)
			yield line.rstrip() + '<br/>\n'
	return Response(inner(), minetype='text/html')



if __name__ == "__main__":
	app.run(debug=True)
