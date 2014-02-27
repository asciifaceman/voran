from flask imoprt Flask

@app.route("/")
def hello():
	return "Testing"
if __name__ == "__main__":
	app.run()
