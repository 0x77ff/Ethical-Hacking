import tkinter as tk
from encrypt import encrypt

window = tk.Tk()
window.title("Ceaser Cipher")
window.resizable(0,0)
window.geometry("500x500")

def generate():
    print(encrypt(entry1.get(),int(entry2.get())))
    output.config(text=encrypt(entry1.get(),int(entry2.get())))

text1 = tk.Label(window,text='Input Text')
entry1 = tk.Entry(window)
text2= tk.Label(window, text='Insert Shift Ammount')
entry2 = tk.Entry(window)
button1 = tk.Button(window,command=generate)
output = tk.Label(window,text='',width=10,height=5,font=('Bold',24))

text1.pack()
entry1.pack()
text2.pack()
entry2.pack()
button1.pack()
output.pack()
window.mainloop()
