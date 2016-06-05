# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
""" Network and Data Security-MSDS 7349
    Homework 1  - Exercise 2, part 3
    Rahn Lieberman


"""
import zipfile

def checkpw(zipToOpen, pw):
    zf = zipfile.ZipFile(zipToOpen)    
    try:
        zf.extractall('.', pwd=pw)
        return True
    except:
        return False

def main():
    myZip = 'evil.zip'
    commonPW = open('dictionary_of_common_passwords.txt','r') 
    for word in commonPW.readlines():
        #rstrip needed to remove the newline at end of each word
        if (checkpw(myZip,word.rstrip())):
            print('PASSWORD FOUND!  It is: ' + word.rstrip())
            return
        else:
            print ('Password is not: ' + word.rstrip())
        

if __name__ == "__main__":
    main()
    