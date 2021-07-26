import tkinter
import random
from tkinter import messagebox

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

windows=tkinter.Tk()
windows.title("PassGen By Cyber_Hill")
passcout = tkinter.Label(text="Գաղտնաբառերի քանակը",  width=60, foreground='black')
entry = tkinter.Entry(width=60, bg="white", fg="black")
passlen = tkinter.Label(text="Գաղտնաբառերի Երկարությունը",  width=60, foreground='black')
entry1 = tkinter.Entry(width=60, bg="white", fg="black")
s=0
def btn1():

    global s
    cout=entry.get()
    lens=entry1.get()
    # if not cout or not lens:
    #     error = tkinter.Label(text="No", width=60, foreground='Black')
    #     error.pack()
    # button.destroy()
    try:
        cout=int(cout)
        lens=int(lens)

        if s ==0:
            global greeting
            greeting = tkinter.Text(background="black", width=60, foreground='white',state='disabled')
            greeting.pack()
            s+=1
        if s>0:
            greeting.destroy()
            greeting = tkinter.Text(background="black", width=60, foreground='white')
            greeting.pack()
        for n in range(cout):
            password = ''
            for i in range(lens):
                password += random.choice(chars)
            greeting.insert("1.0",password+f"\n---------------"+f"\n")
        greeting.configure(state=tkinter.DISABLED)



    except:
        messagebox.showerror("Սխալ", "Դաշտերը դատարկ են կամ մուտքագրվածը թիվ չէ")
button = tkinter.Button(
    text="Գեներացնել",
    width=15,
    height=1,
    bg="blue",
    fg="yellow",
    command=btn1
)
passcout.pack()
entry.pack()
passlen.pack()
entry1.pack()
button.pack()
windows.mainloop()