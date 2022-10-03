from  tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width = 500, height =300)

my_label = Label(text = "My first label", font = ("Times New Roman", 24, "bold"))
my_label.pack()

# changing labels by using either these two methods:-
my_label["text"]  = "My label"
#my_label.config(text = "Hello")


# creating afunction to change the label when the button is clicked.

def change_config():
    #my_label.config(text = "Hello")
    my_label.config(text = entry.get())
# Buttons
button = Button(text = "click me", command = change_config)
button.pack()

# Entry
entry = Entry(width = 10)

entry.pack()
#entry.get()







window.mainloop()  # this will keep the window on screen.
