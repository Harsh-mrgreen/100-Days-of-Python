from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(width = 300, height =100)
window.config(padx= 20, pady= 20)


entry = Entry(width=5)
#Add some text to begin with
entry.insert(END, string= 0)
#Gets text in entry
#rint(entry.get())
entry.place(x =120, y = 10)


#Labels
label = Label(text="Miles")
label.place(x = 170, y = 10)


label_1 = Label(text="is equal to")
label_1.place(x = 40, y = 30)

label_2 = Label(text= 0)
label_2.place(x = 130, y = 30)

label_3 =Label(text= "Km")
label_3.place(x = 175, y = 30)

def change_label():
    input = float(entry.get())
    label_2.config(text= input * 1.6)

button = Button(text="Calculate", command=change_label)
button.place(x = 110, y = 50)

window.mainloop()