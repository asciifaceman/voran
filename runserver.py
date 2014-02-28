# This is ONLY to run Voran as a local service (127.0.0.1:5000)
# This particular script is for bootstrapping management interfaces
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from voran import app

manager = Manager(app)

# Turn on debugging by default and reloader (typcial behaviour)
manager.add_command("runserver", Server(
	use_debugger = True,
	use_reloader = True,
	host = '0.0.0.0')
)

if __name__ == "__main__":
	manager.run()

#app.run(debug=True)