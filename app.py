from flask import Flask

from web.controller import configure

app = Flask(__name__)
configure(app).run()
