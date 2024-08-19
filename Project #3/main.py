import customtkinter as ctk
import random
import string

class PasswordGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up the GUI
        self.title("Password Generator")
        self.geometry("350x350")

        # Create input fields for user parameters
        self.min_length_label = ctk.CTkLabel(self, text="Minimum length for password:")
        self.min_length_label.pack(pady=10)
        self.min_length_entry = ctk.CTkEntry(self, width=100)
        self.min_length_entry.pack()

        self.has_number_label = ctk.CTkLabel(self, text="Do you want numbers in it? (Y/N):")
        self.has_number_label.pack(pady=10)
        self.has_number_checkbox = ctk.CTkCheckBox(self, text="Yes")
        self.has_number_checkbox.pack()

        self.has_special_label = ctk.CTkLabel(self, text="Do you want special characters in it? (Y/N):")
        self.has_special_label.pack(pady=10)
        self.has_special_checkbox = ctk.CTkCheckBox(self, text="Yes")
        self.has_special_checkbox.pack()

        # Create button to generate password
        self.generate_button = ctk.CTkButton(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Create label to display generated password
        self.password_label = ctk.CTkLabel(self, text="")
        self.password_label.pack()

    def generate_password(self):
        # Get user input from GUI
        min_length = int(self.min_length_entry.get())
        has_number = self.has_number_checkbox.get()
        has_special = self.has_special_checkbox.get()

        # Function for password generation and choice between length, numbers and characters
        def gen_pass(min_length, numbers=True, special_characters=True):
            letters = string.ascii_letters
            digits = string.digits
            special = string.punctuation

            characters = letters
            if numbers:
                characters += digits
            if special_characters:
                characters += special

            pwd = ""
            meet_criteria = False
            has_number = False
            has_special = False

            while not meet_criteria or len(pwd) < min_length:
                new_char = random.choice(characters)
                pwd += new_char

                if new_char in digits:
                    has_number = True
                elif new_char in special:
                    has_special = True

                meet_criteria = True
                if numbers:
                    meet_criteria = has_number
                if special_characters:
                    meet_criteria = meet_criteria and has_special

            return pwd

        # Generate password
        pwd = gen_pass(min_length, has_number, has_special)

        # Display generated password
        self.password_label.configure(text="Your generated password is: " + pwd)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()