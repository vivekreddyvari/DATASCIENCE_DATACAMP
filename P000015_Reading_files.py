# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:40:08 2019

@author: M63A520
"""

from sys import argv
script = argv
#filename = "C:\Users\m63a520\Python\P000015_example"
txt = open(script)
print("Here's your file %r:" % script)
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())