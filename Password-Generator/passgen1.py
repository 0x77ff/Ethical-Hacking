import secrets
import string
import pyperclip

amt=input('>Enter Password Length: ')
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
    generatepass(amt)  
       
    
