import secrets
import string
import pyperclip

lenamt=input('>Enter Password Length: ')
passamt=input('>Enter Password Amount: ')
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet= letters+digits+special_chars
password=' '
multipassword=[ ]

def generatepass(length,pamt):
    global password
    global multipassword
    for i in range(int(pamt)):
     print(password)
    #pyperclip.copy(password)
     password=''
     for i in range(int(length)):
         password += ''.join(secrets.choice(alphabet))
    print(password) 
     

if __name__ == '__main__':
    generatepass(lenamt,passamt)  
       
    
