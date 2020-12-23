import pika
import json
import requests


params = pika.URLParameters('amqps://cyqkzrcg:nN77aHPNXDkyJO7_7Xr57ytSB4Qx4itt@vulture.rmq.cloudamqp.com/cyqkzrcg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)
    with requests.Session() as s:
        if properties.content_type == 'product_created':
            s.post('http://172.19.0.3:5000/api/products', json=data)
            
        elif properties.content_type == 'product_updated':
            s.put(f'http://172.19.0.3:5000/api/products/{data["id"]}', json=data)

        elif properties.content_type == 'product_deleted':
            s.delete(f'http://172.19.0.3:5000/api/products/{data}')

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()