import secrets
import string
import pyperclip

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet= letters+digits+special_chars
password=' '

def generatepass(length):
    global password
    for i in range(int(length)):
        password += ''.join(secrets.choice(alphabet))
    print(password) 
    pyperclip.copy(password)  

if __name__ == '__main__':
    generatepass(12)  
       
    
