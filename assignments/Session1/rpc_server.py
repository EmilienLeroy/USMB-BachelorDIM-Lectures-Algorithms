# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:24:47 2017
@brief : RPC Server
@author: leroyem
"""

#!/usr/bin/env python
#import library
import pika
import os

# Configure a connexion to a remote RabbitMQ instance:
amqp_url='amqp://heysvpao:YXXlkTcgaIxuUQCIEEgsqj-n-L1ZwOcp@lark.rmq.cloudamqp.com/heysvpao';
url = os.environ.get('CLOUDAMQP_URL',amqp_url);
params = pika.URLParameters(url);
params.socket_timeout = 5;
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

#Function who response to the client
def on_request(ch, method, props, body):
    print(" [.] Client " +str(body))
    response = 'Find and you?'

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()