import pika

host = 'localhost'
port = 5672
queueIndexingRequests = 'indexing_requests'
queueIndexingResponses = 'indexing_responses'


def get_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host, port=5672))
    return connection


def callback(ch, method, properties, body):
    send_response("ok")


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
                          body=response)
    conn.close()

