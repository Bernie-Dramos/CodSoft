import customtkinter
from tkinter import *
from tkinter import messagebox

app = customtkinter.CTk()
app.title("Contact Book")
app.geometry('500x500')
app.config(bg='#2f2f2f')

font1 = ('Roboto Condensed Regular', 30, 'bold')
font2 = ('Roboto Condensed Regular', 18, 'bold')
font3 = ('Roboto Condensed Regular', 10, 'bold')

contact_count = 0
selected_contact = ""

def new_contact():
    global contact_count
    name = contact_name_entry.get()
    number = contact_number_entry.get()
    if name and number:
        with open('contacts.txt', 'a') as f:
            f.write(f"{name}: {number}\n")
        contact_name_entry.delete(0, END)
        contact_number_entry.delete(0, END)
        contact_count += 1
        total_label.config(text=f"Total number of contacts: {contact_count}")
    else:
        messagebox.showerror("Error", "Please enter both name and number")

def delete_contact():
    global contact_count
    global selected_contact
    if selected_contact:
        with open('contacts.txt', 'r') as f:
            lines = f.readlines()
        with open('contacts.txt', 'w') as f:
            for line in lines:
                if line.strip() != selected_contact:
                    f.write(line)
        contact_name_entry.delete(0, END)
        contact_number_entry.delete(0, END)
        contact_count -= 1
        total_label.config(text=f"Total number of contacts: {contact_count}")
        selected_contact = ""
        result_label.config(text="")
        delete_contact_button.place_forget()
    else:
        messagebox.showerror("Error", "Please select a contact to delete")

def search_contact():
    global selected_contact
    name = search_entry.get()
    with open('contacts.txt', 'r') as f:
        lines = f.readlines()
    found = False
    for line in lines:
        if name in line:
            result_label.config(text=f"Found: {line.strip()}")
            selected_contact = line.strip()
            found = True
            delete_contact_button.place(x=170, y=410)
            break
    if not found:
        result_label.config(text="Contact not found")
        delete_contact_button.place_forget()

title_label = customtkinter.CTkLabel(app, text="Contact Book", font=('Roboto Condensed Regular', 40, 'bold'), fg_color='#2f2f2f', text_color='#fff')
title_label.place(y=10, x=20)

contact_name_label = customtkinter.CTkLabel(app, text="Name:", font=font2, fg_color='#2f2f2f', text_color='#fff')
contact_name_label.place(x=20, y=80)

contact_name_entry = customtkinter.CTkEntry(app, placeholder_text="Name", font=font1, text_color='#fff', border_width=2, width=300, fg_color='#2f2f2f')
contact_name_entry.place(y=110, x=20)

contact_number_label = customtkinter.CTkLabel(app, text="Number:", font=font2, fg_color='#2f2f2f', text_color='#fff')
contact_number_label.place(x=20, y=160)

contact_number_entry = customtkinter.CTkEntry(app, placeholder_text="Number", font=font1, text_color='#fff', border_width=2, width=300, fg_color='#2f2f2f')
contact_number_entry.place(y=190, x=20)

add_contact = customtkinter.CTkButton(app, command=new_contact, font=font2, text="Add Contact", fg_color='#03055B', hover_color='#333')
add_contact.place(x=20, y=240)

search_label = customtkinter.CTkLabel(app, text="Search for a contact:", font=font2, fg_color='#2f2f2f', text_color='#fff')
search_label.place(x=20, y=300)

search_entry = customtkinter.CTkEntry(app, placeholder_text="Name", font=font1, text_color='#fff', border_width=2, width=300, fg_color='#2f2f2f')
search_entry.place(y=330, x=20)

search_button = customtkinter.CTkButton(app, command=search_contact, font=font2, text="Search Contact", fg_color='#03055B', hover_color='#333')
search_button.place(x=20, y=380)

result_label = customtkinter.CTkLabel(app, text="", font=font2, fg_color='#2f2f2f', text_color='#fff')
result_label.place(x=20, y=350)

delete_contact_button = customtkinter.CTkButton(app, command=delete_contact, font=font2, text="Delete", fg_color='#03055B', hover_color='#333')

total_label = customtkinter.CTkLabel(app, text="Total number of contacts: 0", font=font2, fg_color='#2f2f2f', text_color='#fff')
total_label.place(x=20, y=420)

try:
    with open('contacts.txt', 'r') as f:
        lines = f.readlines()
        contact_count = len(lines)
        total_label.config
except FileNotFoundError:
    with open('contacts.txt', 'w') as f:
        pass

app.mainloop()