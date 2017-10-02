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
    if som == 0:
        average= 0;
        return float(average)
    #compute the final average
    else:
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

#Random item selection
def shuffle(shufflelist):
    #@details Function able to shuffle a list
    #@param list; the lsit that will be shuffle 
    
    #init variable
    copylist = [];
    i = 0;
    randomlist = [];
    random = randint(0,(len(shufflelist))-1);

    #copy the initial list
    for l in shufflelist:
        copylist.append(l);   
    
    #retrieve 'x' random number
    for r in range(0,len(shufflelist)):
            random = randint(0,(len(shufflelist))-1);
            while random in randomlist != True:
                    random = randint(0,(len(shufflelist))-1);           
            randomlist.append(random)    
    
    #shuffle the initial list
    for li in randomlist:
        shufflelist[i]=copylist[li];
        i=i+1;      
    
    #@return the list shuffle
    return shufflelist; 

'''
#Testing shuffle function
mylist = [1,2,3,5,6,3]
ls = shuffle(mylist)
print ls
'''

#Sorting

def sort_selective(list_in):
    #@details Function able to sort a list
    #@param list; the lsit that will be sort 
    
    #init variable
    list_lenght = len(list_in);
    Svector = [];
    maxi = 0;
    
    #Sort the list
    for l in range(0,list_lenght):
        maxi = max_value(list_in);
        Svector.append(maxi);
        list_in.remove(maxi);
        
    #@return the list sort
    return Svector;


'''
#Testing sort_selective function
vector = [10, 15, 7, 1,3, 3, 9];
svector = sort_selective(vector);
print svector

#Question
Does the number of iterations depend on the vector content ?
Yes.

How many iterations are required to sort the whole vector ?
The number of iterations depends on the size of the vector.
Here 7.

How many permutations are applied ?
As much as the number of values ​​in the vector.
Here 7.

How many comparisons are applied ?
As much as the number of values ​​in the vector.
Here 7.

Can you quantify the algorithm complexity ?
Not very complex.
'''

def sort_bubble(list_in):
    #@details Function able to sort a list
    #@param list; the lsit that will be sort 
    
    #init variable
    N = len(list_in)-1;
    change = True;
    
    #Sort the list with the bubble algorithm
    while N > 0 and change == True:
        change = False;
        for j in range(0,N):
            if list_in[j]>list_in[j+1]:
                change = True;
                temp = list_in[j];
                list_in[j] = list_in[j+1];
                list_in[j+1] = temp;
        N = N - 1;
        maxi = max_value(list_in);
        list_in.remove(maxi);
        list_in.append(maxi); 
    
    #@return the list sort    
    return list_in;

'''
#Testing sort_bubble function
vector = [10, 15, 7, 1,3, 3, 9];
svector = sort_bubble(vector);
print svector

#Question
Does the number of iterations depend on the vector content ?
No.

How many iterations are required to sort the whole vector ?
the number of iterations depends on the values ​​in the vector.
Here 17.

How many permutations are applied ?
this depends on the values ​​in the vector.
Here 17.

How many comparisons are applied ?
this depends on the values ​​in the vector
Here 13.

Can you quantify the algorithm complexity ?
Very complex.

'''