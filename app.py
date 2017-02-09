# import threading
#
from flask import Flask

from messaging.rabbit import begin_consuming

#
from service.classificationService import classify_image
from web.controller import configure

# rabbitThread = threading.Thread(target=begin_consuming)
# rabbitThread.start()
#
# app = Flask(__name__)
#
# configure(app).run()


classify_image("/home/gzhebrakov/Pictures/20160616-SummerParty/IMG_4013_1.jpg")

