from Views.views import app_store
from flask import Flask, jsonify, url_for, redirect, request,abort
app = Flask(__name__)
app.register_blueprint(app_store)

if __name__ == '__main__':
    app.run(debug=True)
