import os

# Flask options
FLASK_HOST = os.environ['FLASK_HOST']
FLASK_PORT = int(os.environ['FLASK_PORT'])

# DB options
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_NAME = os.environ['DB_NAME']
