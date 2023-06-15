from encrypt import encrypt

text=input('>Enter text:')
step=int(input('>Enter Shift Amount:'))
strtext=' '

print(strtext.join(map(str,encrypt(text,step))))