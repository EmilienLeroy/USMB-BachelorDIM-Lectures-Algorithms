# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 10:48:09 2017

@author: leroyem
"""

import S1_algotools as algo


def test_average_above_zero():
    mylist=[1,2,3,4,-7];
    assert algo.average_above_zero(mylist) == 2.5;
    
    mylist=[1,1,1,1];
    assert algo.average_above_zero(mylist) == 1;
    
    mylist=[-5,-4,-2,-4];
    assert algo.average_above_zero(mylist) == 0;
    
    mylist=[-5,25,100,-40];
    assert algo.average_above_zero(mylist) == 62.5;
    
    mylist=[0,0,0,0];
    assert algo.average_above_zero(mylist) == 0;
    

def test_max_value():
    mylist=[1,-3,25];
    assert algo.max_value(mylist) == 25;
    
    mylist=[-1,-3,-25];
    assert algo.max_value(mylist) == -1;
    
    mylist=[0,0,0];
    assert algo.max_value(mylist) == 0;
    
    mylist=[25];
    assert algo.max_value(mylist) == 25;

def test_reverse_table():
    mylist=[1,-3,25,5,6,7,9];
    newlist=[9, 7, 6, 5, 25, -3, 1];
    assert algo.reverse_table(mylist)==newlist;
    
    mylist=[0,0,0,0];
    newlist=[0,0,0,0];
    assert algo.reverse_table(mylist)==newlist; 
    

    
    