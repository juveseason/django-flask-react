import pika, json, os, django
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from django.conf import settings

params = pika.URLParameters(settings.AMQP_URI)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    with requests.Session() as s:
        endpoint = f'http://{settings.DOCKER_LOCALHOST}:8000/api/products/{id}'
        s.put(endpoint, json={'likes': 1})

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()