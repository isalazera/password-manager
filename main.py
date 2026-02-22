from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    input_password.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = input_website.get()
    password = input_password.get()
    username = input_username.get()

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        is_ok = messagebox.askyesno(title=f"{website}", message=f"These are the details entered: \nEmail or Username: {username}\nPassword: {password}")
        if is_ok == True:
            with open("data.txt","a", encoding="utf-8") as file:
                file.write(f"{website} | {username} | {password} \n")
            messagebox.showinfo("Password Added", "Password has been added")
            input_website.delete(0, END)
            input_password.delete(0, END)
            input_website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(window, text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(window, text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(window, text="Password:")
password_label.grid(column=0, row=3)

#Entries
input_website = Entry(width=50)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_username = Entry(width=50)
input_username.grid(column=1, row=2, columnspan=2)
input_username.insert(0, "ilazera@email.com")

input_password = Entry(width=25)
input_password.grid(column=1, row=3, columnspan=1)

#Buttons
generate_button = Button(text="Generate Password",width=20, command=gen_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=42, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()