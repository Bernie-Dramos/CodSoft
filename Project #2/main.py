# Call any libraries or resources needed to initialize the app
import customtkinter
from tkinter import *
from tkinter import messagebox

# Initialize the GUI app and its size
app = customtkinter.CTk()
app.title("Calculator")
app.geometry('300x300')
app.config(bg='#000')

# Set fonts to be used
font1 = ('Roboto Condensed Regular', 20, 'bold')

# Creating the functions for the buttons, clear and calculate
def button_press(number):
    eq_entry.insert(END, number)
    
def clear():
    eq_entry.delete(0, END)
    
def calculate():
    try:
        result = eval(eq_entry.get())
        clear()
        eq_entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except:
        messagebox.showerror("Error", "Invalid input!")
        
# Create the entry box where the numbers and results are shown
eq_entry = customtkinter.CTkEntry(app, font=font1, text_color='#fff', fg_color='#000', border_color='#fff', width=280, height=60)
eq_entry.place(x=10, y=10)

# Create the butons and their functions
b1 = customtkinter.CTkButton(app, command=lambda: button_press('7'), font=font1, text_color='#fff', text="7", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b1.place(x=10, y=80)

b2 = customtkinter.CTkButton(app, command=lambda: button_press('8'), font=font1, text_color='#fff', text="8", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b2.place(x=80, y=80)

b3 = customtkinter.CTkButton(app, command=lambda: button_press('9'), font=font1, text_color='#fff', text="9", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b3.place(x=150, y=80)

b4 = customtkinter.CTkButton(app, command=lambda: button_press('4'), font=font1, text_color='#fff', text="4", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b4.place(x=10, y=125)

b5 = customtkinter.CTkButton(app, command=lambda: button_press('5'), font=font1, text_color='#fff', text="5", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b5.place(x=80, y=125)

b6 = customtkinter.CTkButton(app, command=lambda: button_press('6'), font=font1, text_color='#fff', text="6", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b6.place(x=150, y=125)

b7 = customtkinter.CTkButton(app, command=lambda: button_press('1'), font=font1, text_color='#fff', text="1", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b7.place(x=10, y=170)

b8 = customtkinter.CTkButton(app, command=lambda: button_press('2'), font=font1, text_color='#fff', text="2", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b8.place(x=80, y=170)

b9 = customtkinter.CTkButton(app, command=lambda: button_press('3'), font=font1, text_color='#fff', text="3", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b9.place(x=150, y=170)

b10 = customtkinter.CTkButton(app, command=lambda: button_press('0'), font=font1, text_color='#fff', text="0", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b10.place(x=10, y=215)

b11 = customtkinter.CTkButton(app, command=lambda: button_press('.'), font=font1, text_color='#fff', text=".", fg_color='#323d3b', hover_color='#05b314', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b11.place(x=80, y=215)

b12 = customtkinter.CTkButton(app, command=clear, font=font1, text_color='#fff', text="C", fg_color='#e33805', hover_color='#9e2703', bg_color='#000', border_color='#fff', border_width=2, cursor='hand2', width=60)
b12.place(x=150, y=215)

b13 = customtkinter.CTkButton(app, command=calculate, font=font1, text_color='#fff', text="=", fg_color='#05b00e', hover_color='#027d09', bg_color='#000', border_color='#fff', corner_radius=10, cursor='hand2', width=280)
b13.place(x=10, y=255)

b14 = customtkinter.CTkButton(app, command=lambda: button_press('+'), font=font1, text_color='#fff', text="+", fg_color='#c20486', hover_color='#8a035f', bg_color='#000', border_color='#fff', corner_radius=10, cursor='hand2', width=60)
b14.place(x=220, y=80)

b15 = customtkinter.CTkButton(app, command=lambda: button_press('-'), font=font1, text_color='#fff', text="-", fg_color='#c20486', hover_color='#8a035f', bg_color='#000', border_color='#fff', corner_radius=10, cursor='hand2', width=60)
b15.place(x=220, y=125)

b16 = customtkinter.CTkButton(app, command=lambda: button_press('*'), font=font1, text_color='#fff', text="*", fg_color='#c20486', hover_color='#8a035f', bg_color='#000', border_color='#fff', corner_radius=10, cursor='hand2', width=60)
b16.place(x=220, y=170)

b17 = customtkinter.CTkButton(app, command=lambda: button_press('/'), font=font1, text_color='#fff', text="/", fg_color='#c20486', hover_color='#8a035f', bg_color='#000', border_color='#fff', corner_radius=10, cursor='hand2', width=60)
b17.place(x=220, y=215)



# Executes the app to run continously until it's exited
app.mainloop()