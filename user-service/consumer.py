import os
import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

import pika 
import json
import logging
from  consume_utils import  tenant_callback

username = os.getenv('RABBITMQ_DEFAULT_USER' , 'root')
password = os.getenv('RABBITMQ_DEFAULT_PASS' , 'root')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        'rabbitmq',
        5672,
        '/',
        credentials=pika.PlainCredentials(username, password)
    )


)
channel = connection.channel()
channel.exchange_declare(exchange='appevents', exchange_type='topic', durable=True)


def callback(ch, method, properties, body):
    routing_key = method.routing_key
    contenttype = routing_key.split('.')[1]
    event_type = routing_key.split('.')[-1]
    data = json.loads(body)
   

    if contenttype == 'tenant':
        tenant_callback(ch , event_type , data , method)
        logging.info('tenant callback done')
    else:
        logging.warning(f"Unhandled content type: {contenttype}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)



channel.queue_declare('user-service' , durable=True , )
channel.queue_bind('user-service', 'appevents', 'app.*.*')
channel.basic_consume(queue='user-service', on_message_callback=callback, auto_ack=False)



channel.start_consuming()
