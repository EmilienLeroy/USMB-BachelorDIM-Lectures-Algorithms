# -*- coding: utf-8 -*-
"""
@author : Emilien Leroy, LP DIM
@brief : a set of generic functions for data management  
"""
"""
#a variable
a=1 # default type : int

#an empty list
mylist = []

#a filled list
mylist2 = [1,2,3]

#append to a list 
mylist.append(10)

#a buggy list
mybuggylist=[1,'a',"Hi"]

#operators
b=a+2
mylist_sum=mylist+mylist2
"""

def average_above_zero(input_list):
     
    #init variable
    som = 0
    n = 0
    
    #compute the average of positive elements of a list
    for item in input_list:
        if item > 0:
            som = som + item
            n = n+1
        elif item==0:
            print('This value is null:'+str(item))        
        else:
            print('This value is not positive:'+str(item))
    #compute the final average
    average= float(som)/float(n)
    print('Positive elements average is '+str(average))
    return float(average)
    
"""    
#testing the fonction
mylist=[1,2,3,4,-7]
result=average_above_zero(mylist)
message="The average of positive sample of {list_value} is {res}".format(list_value=mylist,res=result)
print(message)
"""

def max_value(input_list):
    ##
    #@details Basic function able to return the max value of a list
    #@param input_list; the input list to be scanned
    #@Throws an exception (ValueError) on an empty list 

    #first check if provided list is no empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init variable
    max_value=input_list[0]
    #compute the average of positive elements of a list
    for item in input_list:
        if max_value<item:
            max_value=item
    #@return the max value
    return max_value
    
    

""" 
#testing max_value fonction
mylist=[1,-3,25]
mymax=max_value(mylist)
message=('Max Value of {input_l} is {max_v}'.format(input_l=mylist,max_v=mymax))
print(message)

"""
def reverse_table(input_list):
    #@details Basic function able to reverse a table
    #@param input_list; the input list to be scanned
    #@Throws an exception (ValueError) on an empty list
    
    #first check if provided list is no empty
    if len(input_list)==0:
        raise ValueError('provided list is empty')
    #init variable
    last_idx=len(input_list)
    #reverse a table
    for idx in range(len(input_list)/2):
        last_idx-=1
        reverse = input_list[idx]
        input_list[idx]=input_list[last_idx]
        input_list[last_idx]=reverse
        #@return reverse table 
        return input_list
 
"""
#testing reverse fonction       
mylist=[1,-3,25,5,6,7,9]
mlist=reverse_table(mylist)
print(mylist)
"""
#matrix processing lib
import numpy

def roi_bbox(myMat):
    #@details Function able to find xmin xmax ymin ymax
    #@param myMat; the matrix or the image 
    

    #init variable
    size_rows=10
    size_cols=10
    xmin=size_cols
    xmax=0
    ymin=size_rows
    ymax=0
    
    #Check all the matrix to find the min and max
    for row in range(0,size_rows):
        for cols in range(0,size_cols):
            if myMat[row,cols] == 1:
                if xmin > row:
                    xmin = row
                if xmax < row:
                    xmax = row
                if ymin > cols:
                    ymin = cols
                if ymax < cols:
                    ymax = cols
                
    #@return Output coordinates matrix
    bbox_coords=numpy.array([[ymin,xmin],[ymin,xmax],[ymax,xmin],[ymax,xmax]])
    return bbox_coords
 


   
#filling something in the matrix. The basic way
"""
for row in range(5,8):
for cols in range(7,9):
myMat[row,cols]=1
"""
"""
#Testing Matrix Function
#Create a matrix
myMat=numpy.zeros([10,10],dtype=int)
#filling something in the matrix. A nicer way
myMat[2:4,5:9]=numpy.ones([2,4])
reponse=roi_bbox(myMat)
print reponse
print myMat
"""


#Random Table
#random processing lib
from random import *

def random_fill_sparse(tab, v):
    #@details Function able to fill randomly a matrix
    #@param tab; the table
    #@param v; a random number
    
    #init variable
    size_tab = len(tab);
    counter = 0;
    
    #Fill the table until the counter is equal to zero
    for row in range(0,size_tab):
        for cols in range(0,size_tab):
            if counter < v:
                tab[row,cols]='X';
                counter=counter+1;    
    #@return the table fill           
    return tab;
                
def alea(v):
    #@details Function who return an random number 
    #@param v; the size of the array
    random = randint(0,v); 
    return random;
    
"""
#Testing random_fill_sparse function
n=5;
tab=numpy.chararray((n, n));
tab[:] = '';
v= tab.size;
random = alea(v);
result = random_fill_sparse(tab,random);
print result;
"""

#Remove Whitespace
def remove_whitespace(string):
    #@details Function able to remove whitespace in a string
    #@param string; the string with the whitespace  
    
    #init variable
    temp = "";
    
    #Parse the string and find the whitespace
    for chara in string:
        if chara != " ":
            temp = temp + chara;
    #@return the string without whitespace
    return temp; 

"""
#Testing remove_whitespace function
whitespace = "I am a whitespace";
result = remove_whitespace(whitespace);
print(result);
"""


           



        
        
     
       
      