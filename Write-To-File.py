#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:33:35 2019

@author: joseph
"""
print("Let us see how to write to the file")
"""
To write to file, we need to do 
(1) create a file if file not there  or open a file if the fie exist
(2) write to the file
(c) close the file
"""
#  Step 1 You opened a file or create a file for writing
mywriting = open("myfile.txt","w+")
print(type(mywriting))
# step 2 write to the file 

mywriting.write("Hello I a writing to this file ")

# step 3 close the file 
mywriting.close()

"""
Lets see how to append to a file

""" 
myappend = open("appendmyfile.txt","a+")
myappend.write("Here I am appending to a file\n")
myappend.close()


