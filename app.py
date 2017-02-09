# import threading
#
from flask import Flask

from messaging.rabbit import begin_consuming

#
from service.classificationService import classify_image
from web.controller import configure

begin_consuming()
# rabbitThread = threading.Thread(target=begin_consuming)
# rabbitThread.start()
#
# app = Flask(__name__)
#
# configure(app).run()


#classify_image("/home/dominator/Desktop/1486567387_1.jpg")

