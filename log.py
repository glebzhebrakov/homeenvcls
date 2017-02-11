import logging


def setup_custom_logger(name):
    logging.basicConfig(
        level=logging.INFO,
        filename="homeenvcls.log",
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s',
    )

    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)

    return logger
