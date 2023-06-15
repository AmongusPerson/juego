from tkinter import *
import random
pg = Tk()
pg.geometry("500x500")
pg.title("Adivina un Numero del 1 al 100")
pg.configure(background="#a8dadc")


def fn1():
    global gl1
    gl1 = random.randint(1,100)
    guesses_left.set(10)
    vr1 = int(ip1.get)
    if vr1 == gl1:
        lb2["text"] = "¡Ganaste!"
    elif guesses_left <= 0:
        lb2["text"] = "Perdiste"
    elif vr1 > gl1:
        lb2["text"] = "El numero es menor"
        guesses_left.set(guesses_left-1)
    else:
        lb3["text"] = "El numero es mayor"
        guesses_left.set(guesses_left-1)


bt1 = Button(pg, text="Ejecutar", command=fn1)
bt1.place(relx=0.5, rely=0.25, anchor=CENTER)


lb1 = Label(pg, text="Adivina un Numero del 1 al 100")
lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

ip1 = Entry(pg, font=200)
ip1.place(relx=0.5, rely=0.15, anchor=CENTER,)

lb2 = Label(pg, text=".")
lb2.place(relx=0.5, rely=0.35, anchor=CENTER)

guesses_left = tk.IntVar()
guesses_left.set(10)




        
        
    
    
    
pg.mainloop()