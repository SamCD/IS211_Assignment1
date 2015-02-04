#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Part 2"""

class Book(object):
    """Creates a book"""

    author = ''
    title = ''
    
    def __init__(self, author, title):

        self.author = author
        self.title = title

        
    def display(self):
        """Displays the book's title and author"""
        
        print "{}, written by {}".format(self.title, self.author)
        
book1 = Book('John Steinbeck','Of Mice and Men')
book2 = Book('Harper Lee','To Kill A Mockingbird')

book1.display()
book2.display()
