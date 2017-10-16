# -*- coding: utf-8 -*-
"""
@author : Emilien Leroy, LP DIM
@brief : Choose to read or send message
"""
#import library
import argparse
import simple_queue_publish as write
import simple_queue_read as read

#Add argument
parser = argparse.ArgumentParser(description='test')
parser.add_argument('-read', action='store_true')
parser.add_argument('-write', action='store_true')
args = parser.parse_args()

#Choose argument
if args.read:
    read.read()
    
if args.write:
    write.write()

    