import logging


def setup_custom_logger(name):
    logging.basicConfig(
        level=logging.DEBUG,
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
