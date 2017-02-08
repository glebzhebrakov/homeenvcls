import threading

from flask import Flask

from messaging.rabbit import begin_consuming
from web.controller import configure

rabbitThread = threading.Thread(target=begin_consuming)
rabbitThread.start()

app = Flask(__name__)

configure(app).run()

