""" Network and Data Security-MSDS 7349
    Homework 1 - Exercise 1
    Rahn Lieberman
    
    References:
    - Violent Python, a cookbook for hackers, forensic analysts, penetration testers a
	    security engineers, by TJ O'Conner
    - Randy Balzer - post to 2DS wall about fcrypt function saved me time. 
    - Cross section collaborative effort. (Names listed in turned in version)

    Improvements:
    The crypt function uses a 2 character salt when using standard DES.
    It has a limited dictionary.  This could be improved to allow for more 
    characters and a longer salt.
    A big problem I see is that the standard DES will use only the first 8 characters
    of the password. 
    Reference: http://php.net/manual/en/function.crypt.php
    
"""

#fcrypt works on Windows, and similar to Crypt on Unix
from fcrypt import crypt

def checkPassword(hashedpw):
    salt = hashedpw[0:2]  #first 2 characters give salt, per spec
    dictFile = open('HW1-dictionary.txt','r') 
    for word in dictFile.readlines():  
        word = word.rstrip()  
        cryptWord = crypt(word,salt)  
        if (cryptWord == hashedpw):   
            print "*** Found Password: "+ word +" *** \n"   
            return True
        
    print "Password Not Found.\n" 
    return False

def main():
    passfile = open('HW1-passwords.txt')
    for line in passfile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptedpw = line.split(':')[1].strip(' ')
            print "Cracking password for user: " + user
            if (checkPassword(cryptedpw)):
                return  #Break when correct PW found.
            

# program entry point
if __name__ == "__main__":
    main()
    
    
    
    