"""
File: filemodel.py
Project 9.5

Data model for a file viewer.  Supports navigation
through the lines of a file. Also suppports insertions,
removals, and replacements of a line at the current position,
and saving the changes to the file.
"""

from linkedlist import LinkedList

class FileModel(object):

    def __init__(self, filename):
        # New instance variable _canModify permits or
        # disallows removals and replacements
        # New instance variable _filename needed to save
        # modifications to the file
    #Add from exercise 4

    def first(self):
    #Add from exercise 4

    def last(self):
    #Add from exercise 4

    def next(self):
    #Add from exercise 4

    def previous(self):
    #Add from exercise 4

    def canModify(self):
        """Returns True if a line can be removed or replaced
        or False otherwise."""


    def insert(self, line):
        """Inserts line at the current position or at the
        end of the list if the position is undefined."""


    def remove(self):
        """Precondition: canModify() returns True"""


    def replace(self, line):
        """Precondition: canModify() returns True"""


    def save(self):
        """Saves the list of lines to a file."""


