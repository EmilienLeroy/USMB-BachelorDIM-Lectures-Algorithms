# -*- coding: utf-8 -*-
"""
@author : Emilien Leroy, LP DIM
@brief : Read message from rabbitmq 
"""

#import library
import pika
import os
import argparse
import time

#Add argument
parser2 = argparse.ArgumentParser(description='r')
parser2.add_argument('-concurrency', action='store_true')
parser2.add_argument('-read', action='store_true')
parser2.add_argument('-write', action='store_true')
args2 = parser2.parse_args()

# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://ofjnyzri:E0GBXkm_oKa99NsiyObUI8ksvUXgA92S@lark.rmq.cloudamqp.com/ofjnyzri';
url = os.environ.get('CLOUDAMQP_URL',amqp_url);
params = pika.URLParameters(url);
params.socket_timeout = 5;
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()

#Function who read message
def read():
    channel.queue_declare(queue='presentation')
    def callback(ch, method, properties, body):
        print (method.delivery_tag)
        print(" [x] Received %r" % (body))
          
    channel.basic_consume(callback,
                          queue='presentation',
                          no_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



def read_routine():
    channel.queue_declare(queue='presentation', durable=False)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    def callback(ch, method, properties, body):
        print (method.delivery_tag)
        print(" [x] Received %r" % body)
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='presentation')
    
    channel.start_consuming()    
    
    
if args2.concurrency:   
    read_routine()