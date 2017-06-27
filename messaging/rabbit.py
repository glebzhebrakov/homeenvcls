import logging
import pika
import json

import time

from service.classificationService import classify_image

host = 'rabbitmq'
port = 5672
queueIndexingRequests = 'indexing_requests'
queueIndexingResponses = 'indexing_responses'

logger = logging.getLogger('homeenvcls')


def get_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host, port=5672))
    return connection


def callback(ch, method, properties, body):
    path = json.loads(body)['path']
    imagehash = json.loads(body)['hash']
    logger.info('analyse image ' + path)

    try:
        send_response({
            'path': path,
            'hash': imagehash,
            'classificationResult': classify_image(path)}
        )
        ch.basic_ack(delivery_tag = method.delivery_tag)
    except Exception as e:
        # logger.warning('Protocol problem: %s', 'connection reset')

        send_response({
            'path': path,
            'hash': imagehash,
            'error': e.message}
        )
        ch.basic_ack(delivery_tag = method.delivery_tag)
        logger.error(e)


def begin_consuming():

    while True:
        try:
            logger.info("Connecting to rabbit")
            conn = get_connection()
            channel = conn.channel()
            channel.basic_consume(callback,
                                  queue=queueIndexingRequests,
                                  no_ack=False)
            channel.start_consuming()
        except Exception as e:
            logger.error("Lost connection, reconnecting")
            logger.error(e)
            time.sleep(10)
        continue


def send_response(response):
    conn = get_connection()
    channel = conn.channel()
    channel.basic_publish(exchange='',
                          routing_key=queueIndexingResponses,
                          body=json.dumps(response))

    conn.close()

