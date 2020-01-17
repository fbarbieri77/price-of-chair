__author__ = 'jslvtr'

URL = os.environ.get('MAILGUN_URL')
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"

old-url = "https://api.mailgun.net/v3/<>.mailgun.org/messages"
old-API_KEY = "key-<>"
old-FROM = "Mailgun Sandbox <postmaster@<>.mailgun.org>"
