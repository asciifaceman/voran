from voran import app
from flask import Flask

appName = "Voran Playground"

@app.route("/")
def hello():
	return "Testing"


if __name__ == "__main__":
	app.run(debug=True)
