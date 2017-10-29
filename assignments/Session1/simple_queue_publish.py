# -*- coding: utf-8 -*-
"""
@author : Emilien Leroy, LP DIM
@brief : Send message at rabbitmq
"""
#Files who send message
#import library
import pika
import os
import argparse
import time

#Add argument
parser1 = argparse.ArgumentParser(description='s')
parser1.add_argument('-concurrency', action='store_true')
parser1.add_argument('-read', action='store_true')
parser1.add_argument('-write', action='store_true')
args1 = parser1.parse_args()

# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://ofjnyzri:E0GBXkm_oKa99NsiyObUI8ksvUXgA92S@lark.rmq.cloudamqp.com/ofjnyzri';
url = os.environ.get('CLOUDAMQP_URL',amqp_url);
params = pika.URLParameters(url);
params.socket_timeout = 5;
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()

#sending 1000 message



#function who send the message
def write():
    channel.queue_declare(queue='presentation')
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='Eleroy')
    print(" [x] Sent 'Eleroy'")
    
    
def write_routine(i):
    channel.queue_declare(queue='presentation')
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body=i,
                          properties=pika.BasicProperties(
                           delivery_mode = 2, # make message persistent
                          ))
    print(i)
    
    
if args1.concurrency:
    for i in range (0,100):
        message = "Message numero %r"% (i)
        write_routine(message)
        

connection.close()