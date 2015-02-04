#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Part 1"""


def listDivide(numbers, divide=2):
    """Dividing function
    Args: numbers (list): a list of numbers
        divide (int): a divisor
 
    Ex: listDivide([1,2,3,4,5])
    >>  2
    """
    
    retlist = []
    for i in numbers:
        if i % divide == 0:
            retlist.append(i)
    return len(retlist)


class ListDivideException(Exception):
    """Custom error class for listDivide() function"""
    
    def __init__(self, msg):
        
        self.msg = msg
        
        
def testListDivide():
    """Tests the listDivide() function using set examples.
    If listDivide() function is working properly, returns nothin.
    Otherwise, raises ListDivideException. """
    
    tests = [([1,2,3,4,5],2,2), ([2,4,6,8,10],2,5),
    ([30, 54, 63,98, 100],10,2),([],2, 0),([1,2,3,4,5], 1, 5)]
    for i in tests:
        if listDivide(i[0], i[1]) != i[2]:
            raise ListDivideException("failed test")

if __name__ == 'main':
    testListDivide()
