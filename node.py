# Copyright (C) by Brett Kromkamp 2011-2014 (brett@youprogramming.com)
# You Programming (http://www.youprogramming.com)
# May 03, 2014

class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []
        self.__parent = ''

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children
        
    @property
    def parent(self):
        return self.__parent

    def add_child(self, identifier):
        self.__children.append(identifier)
        
    def add_parent(self, identifier):
        self.__parent = identifier