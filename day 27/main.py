from  tkinter import *

# creating a function to change the label when the button is clicked.
def change_config():
    #my_label.config(text = "Hello")
    my_label.config(text = entry.get())

window = Tk()
window.title("My First Gui Program")
window.minsize(width = 500, height =300)

my_label = Label(text = "My first label", font = ("Times New Roman", 24, "bold"))
my_label.pack()

# changing labels by using either these two methods:-
my_label["text"]  = "My label"
#my_label.config(text = "Hello")



# Buttons
button = Button(text = "click me", command = change_config)
button.pack()

# Entry
entry = Entry(width = 10)
entry.pack()
#entry.get()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()






window.mainloop()  # this will keep the window on screen.
