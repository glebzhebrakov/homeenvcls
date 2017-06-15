import logging

# from classification.classify_image import classify
from classification.henv_classification import classify

logger = logging.getLogger('homeenvcls')


def classify_image(path):
    try:
        return classify(path)
    except Exception as e:
        # logger.warning('Protocol problem: %s', 'connection reset')
        logger.error(e)
