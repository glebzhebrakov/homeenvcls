# import threading
#
import log
logger = log.setup_custom_logger('homeenvcls')
logger.info('#################### starting homeenv classification worker###########################')

from messaging.rabbit import begin_consuming

begin_consuming()


