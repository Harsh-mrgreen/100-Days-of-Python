from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def gen_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + [random.choice(symbols) for char in range(nr_symbols)] + [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_func():
    web_var = web_entry.get()
    name_var = name_entry.get()
    pass_var = pass_entry.get()

    is_empty= (len(web_var)==0) or (len(pass_var) == 0)
    if is_empty:
        messagebox.showinfo(title= "Error", message="Please dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title= web_var, message=f"There are the details entered: email:{name_var},\npassword:{pass_var}")
        if is_ok:
            with open("passwords.txt", "a") as pass_file:
                pass_file.write(f"{web_var} | {name_var} | {pass_var}\n")
        
                web_entry.delete(0,END)
                name_entry.delete(0,END)
                name_entry.insert(0,"mail.harshvsingh@gmail.com")
                pass_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50, bg = "white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_png = PhotoImage(file= "logo.png")
canvas.create_image(100,100, image = password_png)
canvas.grid(row=0, column=1)

web_label = Label(text= "Website:", highlightthickness=0, bg="white")
web_label.grid(row= 1, column= 0)

name_label = Label(text= "Email/Username:", highlightthickness=0, bg="white")
name_label.grid(row=2, column = 0)

pass_label = Label(text= "Password:", highlightthickness=0, bg="white")
pass_label.grid(row=3, column = 0)

web_entry = Entry(width = 39)
web_entry.grid(row= 1, column=1, columnspan=2)
web_entry.focus()


name_entry = Entry(width = 39)
name_entry.grid(row= 2, column=1, columnspan=2)
name_entry.insert(0,"mail.harshvsingh@gmail.com")

pass_entry = Entry(width = 21)
pass_entry.grid(row= 3, column=1, columnspan=1)

gen_button = Button(text= "Generate Password", width= 14, command = gen_pass)
gen_button.grid(row=3, column=2)

add_button = Button(text= "Add", width=33, command = add_func)
add_button.grid(row= 4, column= 1, columnspan=2)



window.mainloop()