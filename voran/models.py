import datetime
from werkzeug import generate_password_hash, check_password_hash
from flask import url_for
from voran import db


class User(db.Document):
	created_date = db.DateTimeField(default=datetime.datetime.now, required=True)
	uname = db.StringField(max_length=255, required=True)
	shortname = db.StringField(max_length=255, required=True)
	email = db.StringField(max_length=100, required=True)
	isadmin = db.BooleanField(required=True, default=False)
	pwdhash = db.StringField(max_length=255, required=True) # Plain text for the time being

	def __unicode__(self):
		return self.shortname

	meta = {
		'allow_inheritance': True,
		'indexes': ['-created_date', 'uname'],
		'ordering': ['-created_date']
	}
