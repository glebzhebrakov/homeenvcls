import pika
import json

from service.classifyService import classify_image

host = 'localhost'
port = 5672
queueIndexingRequests = 'indexing_requests'
queueIndexingResponses = 'indexing_responses'


def get_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host, port=5672))
    return connection


def callback(ch, method, properties, body):
    print (body)
    resp = {'path': 'ok path'}
    classify_image(json.loads(body)['path'])
    send_response(resp)


def begin_consuming():
    conn = get_connection()
    channel = conn.channel()

    channel.basic_consume(callback,
                          queue=queueIndexingRequests,
                          no_ack=True)
    channel.start_consuming()


def send_response(response):
    conn = get_connection()
    channel = conn.channel()
    channel.basic_publish(exchange='',
                          routing_key=queueIndexingResponses,
                          body=json.dumps(response))
    conn.close()


