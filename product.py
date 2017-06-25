import pika
import sys

user_pwd = pika.PlainCredentials('czh', 'czh')
s_conn = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=user_pwd))
chan = s_conn.channel()
chan.queue_declare(queue='hello')
chan.basic_publish(exchange='', routing_key='hello',body='chenzhuhai, ohyeal')
print("[生产者] send 'hello world")
s_conn.close()
