from flask import Flask
from qsr_app import menu


app = Flask(__name__)
app.register_blueprint(menu.bp)


