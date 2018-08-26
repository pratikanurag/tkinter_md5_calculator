from tkinter import *
import hashlib
def hashpassword(text):
    test = text.encode('utf-8')
    h = hashlib.md5()
    h.update(test)
    return h.hexdigest()    
def evaluate(event):
    res.configure(text = "MD5 encoded String: " + str(hashpassword(entry.get())))
w = Tk()
Label(w, text="Input String and press Enter:").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()

