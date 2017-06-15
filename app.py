# import threading
#

import log
logger = log.setup_custom_logger('homeenvcls')
logger.info('#################### starting homeenv classification worker###########################')



#
from messaging.rabbit import begin_consuming
from service.classificationService import classify_image

# begin_consuming()

classify_image("/home/fox/Pictures/1111/IMG_0996.JPG")



