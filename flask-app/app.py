import configparser
from flask import Flask

config = configparser.RawConfigParser()
config.read('config.properties')

app = Flask(__name__)

if config.getboolean("features", "feature_1"):
	message = "Hello, Maria!"
else:
	message = "Hello, World!"

@app.route('/')
def hello():
    return message

if __name__ == '__main__':
    # Run on all interfaces so it can be exposed outside the container
    app.run(host='0.0.0.0', port=8050)