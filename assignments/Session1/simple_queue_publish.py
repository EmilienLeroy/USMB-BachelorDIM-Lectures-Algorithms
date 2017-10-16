# -*- coding: utf-8 -*-
"""
@author : Emilien Leroy, LP DIM
@brief : Send message at rabbitmq
"""
#Files who send message
#import library
import pika
import os
# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://ofjnyzri:E0GBXkm_oKa99NsiyObUI8ksvUXgA92S@lark.rmq.cloudamqp.com/ofjnyzri';
url = os.environ.get('CLOUDAMQP_URL',amqp_url);
params = pika.URLParameters(url);
params.socket_timeout = 5;
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()

#function who send the message
def write():
    channel.queue_declare(queue='presentation')
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='Eleroy')
    print(" [x] Sent 'Eleroy'")
    connection.close()
    

