# -*- coding: utf-8 -*-
""" Network and Data Security-MSDS 7349
    Homework 1  - Exercise 2
    Rahn Lieberman


 Write a quick script to test the use of the zipﬁle library. 
 After importing the library, instantiate a new ZipFile class by 
 specifying the ﬁlename of the password-protected zip ﬁle (evil.zip). 
 utilize the extractall( ) method and specify the optional parameter 
 for the password (secret). 
 Execute your script and turn in the code and output.
 
"""

import zipfile

zf = zipfile.ZipFile('evil.zip')

print("Part 1: Right Password")
zf.extractall('.',pwd='secret')
print("Files extracted. Check Directory")

print("Part 2: Wrong Password")
try:
    zf.extractall('.', pwd='wrong')
except:
    print ('Wrong Password')


