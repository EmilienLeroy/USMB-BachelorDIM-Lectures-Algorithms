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
    # Basic function able to return the max value of a list
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
    return max_value
    
    

""" 
#testing max_value fonction
mylist=[1,-3,25]
mymax=max_value(mylist)
message=('Max Value of {input_l} is {max_v}'.format(input_l=mylist,max_v=mymax))
print(message)

"""
def reverse_table(input_list):
    #Basic function able to reverse a table
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
        return input_list
 
"""
#testing reverse fonction       
mylist=[1,-3,25,5,6,7,9]
mlist=reverse_table(mylist)
print(mylist)
"""

   
       
        
        
        
        
     