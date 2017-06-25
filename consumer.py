import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=pika.PlainCredentials('czh', 'czh')))
cha  = conn.channel()
cha.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("[消费者] recv %s" % body)

cha.basic_consume(callback, queue='hello', no_ack=True)
print('[消费者] waiting for msg.')
cha.start_consuming()
print('陈珠海')
print('sharon1')