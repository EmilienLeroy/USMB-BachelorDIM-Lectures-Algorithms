# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:24:47 2017
@brief : RPC Client
@author: leroyem
"""

#!/usr/bin/env python
#import library
import pika
import uuid
import os
import msgpack 
import msgpack_numpy as m 
import numpy as np #if Numpy is required

#Class Client RPC
class RpcClient(object):
    #Constructor
    def __init__(self):
        # Configure a connexion to a remote RabbitMQ instance:
        amqp_url='amqp://heysvpao:YXXlkTcgaIxuUQCIEEgsqj-n-L1ZwOcp@lark.rmq.cloudamqp.com/heysvpao';
        url = os.environ.get('CLOUDAMQP_URL',amqp_url);
        params = pika.URLParameters(url);
        params.socket_timeout = 5;
        #initiate the connexion
        self.connection = pika.BlockingConnection(params) # Connect to CloudAMQP
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='rpc_queue')
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)
    
    #Function who receive the response of the server
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
    
    #Function who send string to the server
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

#Create new RpcClient object
rpc = RpcClient()
message = np.random.random((20,30))

#encoding the message (array)
encoded_message = msgpack.packb(message,default = m.encode)

#Send and recieve the message
print(" [x] Message:" )
response = rpc.call(encoded_message)
print(" [.] Reponse %r" % response)
