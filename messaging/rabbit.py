import pika
import json

from service.classificationService import classify_image

host = 'localhost'
port = 5672
queueIndexingRequests = 'indexing_requests'
queueIndexingResponses = 'indexing_responses'


def get_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host, port=5672))
    return connection


def callback(ch, method, properties, body):
    path = json.loads(body)['path']
    hash = json.loads(body)['hash']
    print('analyse image ' + path)
    try:
        send_response({
            'path': path,
            'hash': hash,
            'classificationResult': classify_image(path)}
        )
    except Exception as e:
        print e


def begin_consuming():
    conn = get_connection()
    channel = conn.channel()

    channel.basic_consume(callback,
                          queue=queueIndexingRequests,
                          no_ack=True)
    try:
        channel.start_consuming()
    except:
        channel.start_consuming()


def send_response(response):
    conn = get_connection()
    channel = conn.channel()
    channel.basic_publish(exchange='',
                          routing_key=queueIndexingResponses,
                          body=json.dumps(response))
    conn.close()
