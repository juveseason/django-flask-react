import pika
import json

params = pika.URLParameters('amqps://cyqkzrcg:nN77aHPNXDkyJO7_7Xr57ytSB4Qx4itt@vulture.rmq.cloudamqp.com/cyqkzrcg')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)