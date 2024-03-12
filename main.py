from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random

def make_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)


    pass_letters = [choice(letters) for i in range(nr_letters)]

    pass_symbols = [choice(symbols) for x in range(nr_symbols)]

    pass_numbers = [choice(numbers) for y in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)

    password = "".join(password_list)


    pass_entry.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def collect_data():

 website = web_input.get()
 email = em_input.get()
 password = pass_entry.get()
 new_data = {
     website:{
         "email": email,
         "password": password,
     }
 }

 #message box

 if len(website)==0 or len(password)==0:
     messagebox.showinfo(title="oops", message="Don't leave spaces blank!")
 else:
  is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}\nPassword: {password}\n Is it ok to save?")

  if is_ok:

   try:

     with open("data.json", "r") as data_file:

            #reading old data
            data = json.load(data_file)
   except FileNotFoundError:
       with open("data.json", "w") as data_file:
           json.dump(new_data, data_file, indent=4)

   else:
       #updating old data with new data
    data.update(new_data)

    with open ("data.json","w") as data_file:
        #saving the updated data
        json.dump(data, data_file, indent=4)

   finally:
       web_input.delete(0, "end")
       pass_entry.delete(0, "end")


def find_password():
    website = web_input.get()
    try:

        with open("data.json") as file:
         data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="oops", message="Details not found.")

    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]

            messagebox.showinfo(title="Info", message=f"Password: {password}\nEmail: {email}")

        else:
            messagebox.showinfo("Password not found")






        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

#labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
em_label=Label(text="Email/Username:")
em_label.grid(row=2, column=0)
pass_label=Label(text="Password:")
pass_label.grid(row=3, column=0)



#entries

web_input=Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()
em_input =Entry(width=35)
em_input.grid(row=2, column=1, columnspan=2)
em_input.insert(0, "imogen.woodberry@gmail.com")
pass_entry=Entry(width=21)
pass_entry.grid(row=3, column=1)

#buttons
gen_password = Button(text="Generate Password", command=make_password)
gen_password.grid(row=3, column=2)
add = Button(width=36,text="Add", command=collect_data)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command = find_password, width=10)
search.grid(row=1, column=2)









window.mainloop()