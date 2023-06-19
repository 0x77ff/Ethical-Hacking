import secrets
import string

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
generatepass(12)     
