#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/voran/")
#sys.path.insert(0, "/home/asciifaceman/Web/voran/")
#activate_this = '/home/asciifaceman/Web/voran/voran/venv/bin/activate'
activate_this = '/var/www/voran/voran/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from voran import app as application
application.secret_key = "987654321"


