def encrypt(text,step):
    upcase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowcase=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cryptext=[]
    outtext=[]
    for letter in text:
        if letter in upcase:
          index = upcase.index(letter)
          crypt=(index + step) % 26
          cryptext.append(crypt)
          newletter=upcase[crypt]
          outtext.append(newletter)
          
        elif letter in lowcase:
          index = lowcase.index(letter)
          crypt=(index + step) % 26
          cryptext.append(crypt)
          newletter=lowcase[crypt]
          outtext.append(newletter)
    return outtext
  
print(encrypt('ABC',-1))

      