from flask import Flask
from settings import debug
from views import index

app = Flask(__name__)

app.add_url_rule('/', '', index, methods=["GET"])

if __name__ == '__main__':
    app.run(debug=debug)