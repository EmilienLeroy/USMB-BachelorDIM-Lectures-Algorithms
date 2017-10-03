# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:48:09 2017

@author: leroyem
"""

import S1_algotools as algo
import numpy
import pytest
from numpy.testing import assert_array_equal

def test_average_above_zero():
    ##
    #@details Testing aberage_above_zero

    #First basic test
    mylist=[1,2,3,4,-7];
    assert algo.average_above_zero(mylist) == 2.5;
    
    #Test list with the same number
    mylist=[1,1,1,1];
    assert algo.average_above_zero(mylist) == 1;
    
    #Test with only negative value
    mylist=[-5,-4,-2,-4];
    assert algo.average_above_zero(mylist) == 0;
    
    #Test with "big value"
    mylist=[-5,25,100,-40];
    assert algo.average_above_zero(mylist) == 62.5;
    
    #Test with only 0
    mylist=[0,0,0,0];
    assert algo.average_above_zero(mylist) == 0;
    

def test_max_value():
    ##
    #@details Testing max_value

    #First basic test
    mylist=[1,-3,25];
    assert algo.max_value(mylist) == 25;
    
    #Test with only negative value
    mylist=[-1,-3,-25];
    assert algo.max_value(mylist) == -1;
    
    #Test with only 0
    mylist=[0,0,0];
    assert algo.max_value(mylist) == 0;
    
    #test with one number
    mylist=[25];
    assert algo.max_value(mylist) == 25;

def test_reverse_table():
    ##
    #@details Testing reverse table
    
    #First basic test
    mylist=[1,-3,25,5,6,7,9];
    newlist=[9, 7, 6, 5, 25, -3, 1];
    assert algo.reverse_table(mylist)==newlist;
    
    #Test with only zero
    mylist=[0,0,0,0];
    newlist=[0,0,0,0];
    assert algo.reverse_table(mylist)==newlist; 
    
    #Test with no value
    mylist=[];
    newlist=[];
    with pytest.raises(ValueError, match='provided list is empty'):
         algo.reverse_table(mylist)==newlist; 
        
        
def test_roi_bbox():
    ##
    #@details Testing roi bbox

    #First basic test
    myMat=numpy.zeros([10,10],dtype=int)
    myMat[2:4,5:9]=numpy.ones([2,4])
    result=numpy.array([[5,2],[5,3],[8,2],[8,3]])
    assert_array_equal(algo.roi_bbox(myMat),result)
    
    #testing with 0 value
    myMat=numpy.zeros([10,10],dtype=int)
    myMat[0:0,0:0]=numpy.ones([0,0])
    with pytest.raises(ValueError, match='provided matrix is empty'):
        assert_array_equal(algo.roi_bbox(myMat),result)
    
'''
def test_random_fill_sparse():
    n = 10;
    tab=numpy.chararray((n, n));
    v= tab.size;
    random = algo.alea(v);
    result = numpy.chararray((n, n));
    result = numpy.fill((random,random),dtype=numpy.chararray);
    assert_array_equal(algo.random_fill_sparse(tab,random),result)
'''  

def test_remove_whitespace():
    whitespace = "I am a whitespace";
    result = "Iamawhitespace" ;
    assert algo.remove_whitespace(whitespace)==result;
    
    whitespace = "iamnotawhitespace";
    result = "iamnotawhitespace" ;
    assert algo.remove_whitespace(whitespace)==result;
    
    whitespace = "";
    result = "" ;
    assert algo.remove_whitespace(whitespace)==result;
    
def test_shuffle():
    mylist = [1,2];
    assert algo.shuffle(mylist)==[1,2] or [2,1];
    
    mylist = [];
    with pytest.raises(ValueError, match='provided list is empty'):
        algo.shuffle(mylist)==[];