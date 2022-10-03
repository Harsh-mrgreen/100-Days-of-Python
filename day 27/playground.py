from  tkinter import *

from numpy import pad
window = Tk()
window.title("GRID")
window.minsize(width = 500, height =300)
window.config(padx= 20, pady= 20)


my_label = Label(text = "label", font = ("Times New Roman", 24, "bold"))
my_label.grid(row= 0, column= 0)
my_label.config(padx= 30, pady= 30)


button = Button(text="Button")
button.grid(row= 1, column = 1)
button.config(padx= 30, pady= 30)

new_button = Button(text = "new_Button")
new_button.grid(row = 0, column= 2)
new_button.config(padx= 30, pady= 30)

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
#rint(entry.get())
entry.grid(row = 2, column= 3)



window.mainloop()