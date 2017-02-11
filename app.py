# import threading
#

from flask import Flask


import log
logger = log.setup_custom_logger('homeenvcls')
logger.info('#################### starting homeenv classification worker###########################')



#
from messaging.rabbit import begin_consuming
from service.classificationService import classify_image
from web.controller import configure

begin_consuming()
# rabbitThread = threading.Thread(target=begin_consuming)
# rabbitThread.start()
#
# app = Flask(__name__)
#
# configure(app).run()


