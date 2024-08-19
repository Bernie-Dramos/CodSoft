# Call any libraries or resources needed to initialize the app
import customtkinter
from tkinter import *
from tkinter import messagebox

# Set the appeareance of the application
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')

# Initialize the GUI app and its size
root = customtkinter.CTk()
root.title("To-Do List")
root.geometry('1000x750')

# Total number of notes and completed notes
number = 0
completed = 0

# Create a list to store the indices of the done items
done_indices = []

# Set fonts to be used
font1 = ('Roboto Condensed Regular', 30, 'bold')
font2 = ('Roboto Condensed Regular', 18, 'bold')
font3 = ('Roboto Condensed Regular', 10, 'bold')


# Create the function add the new note
def new_note():
    global number 
    note = note_entry.get()
    if note:
        notes_list.insert(0, note)
        note_entry.delete(0, END)
        save_notes()
        number += 1
        total_label.configure(text=f"Total: {number}")
    else:
        messagebox.showerror("Error", "Please enter a note")

# Create a function to delete a note
def delete_note():
    global number, completed
    selected = notes_list.curselection()
    if selected:
        notes_list.delete(selected[0])
        save_notes()
        number -= 1
        total_label.configure(text=f"Total: {number}")
        if selected[0] in done_indices:
            done_indices.remove(selected[0])
            completed -= 1
            complete.configure(text=f"Done: {completed}")
    else:
        messagebox.showerror("Error", "Please select a note to delete")

# Function to save the notes added to a text file
def save_notes():
    with open('notes.txt', 'w') as f:
        notes = notes_list.get(0, END)
        for note in notes:
            f.write(note + '\n')
            
# Function to retrieve the text document witht the saved notes
def get_notes():
    try:
        with open('notes.txt', 'r') as f:
            notes = f.readlines()
            for note in notes:
                notes_list.insert(0, note.strip())
    except FileNotFoundError:
        messagebox.showerror("Error", "No file can be loaded")
    
# Create a function to mark a note as done
def mark_as_done():
    global completed
    selected = notes_list.curselection()
    if selected:
        notes_list.itemconfig(selected[0], bg='green')
        done_indices.append(selected[0])
        completed += 1
        complete.configure(text=f"Done: {completed}")
    else:
        messagebox.showerror("Error", "Please select a note to mark as done")

# Giving the app a frame for aesthetics
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=120, fill='both', expand=True)

# Create a label to display the total number of notes
total_label = customtkinter.CTkLabel(master=frame, text="Total: 0", font=font3)
total_label.place(x=480, y=430)

# Giving the Header namme for the To-Do List
label = customtkinter.CTkLabel(master=frame, text="To-Do List", font=font1)
label.pack(pady=24, padx=20)

# Creating the add note button
add = customtkinter.CTkButton(master=frame,command=new_note, font=font2, text="Add Note")
add.pack(pady=24, padx=20)
add.place(x=310, y=500)

# Create the completed button to mark a task complete
done = customtkinter.CTkButton(master=frame, command=mark_as_done, font=font2, text="Mark as Done")
done.pack(pady=24, padx=20)
done.place(x=80, y=500)

# Create the delete button when a note needs to be removed
delete = customtkinter.CTkButton(master=frame,command=delete_note, font=font2, text="Delete Note")
delete.pack(pady=24, padx=20)
delete.place(x=520, y=500)

# Creating an user input to say what task needs to be done
note_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Add a Note")
note_entry.pack(pady=24, padx=20)

# Create the box to contain and store the notes
notes_list = Listbox(master=frame, width=45, height=15, font=font3, background='grey')
notes_list.pack(pady=24, padx=20)

# Create a label to display the done count
complete = customtkinter.CTkLabel(master=frame, text="Completed: 0", font=font3)
complete.place(x=480, y=460)

# Call the text file to load all the notes already saved
get_notes()
number = notes_list.size()
total_label.configure(text=f"Total: {number}")

# Executes the app to run continously until it's exited
root.mainloop()