import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#800080")

        # Color Palette
        bg_color = "#f0f0f0"
        button_color = "#008080"
        label_color = "#333333"

        # Menu Bar
        self.menubar = tk.Menu(root)
        root.config(menu=self.menubar)

        file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save to Clipboard", command=self.save_to_clipboard)
        file_menu.add_command(label="Save to File", command=self.save_to_file)
        file_menu.add_command(label="Exit", command=root.destroy)

        options_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Options", menu=options_menu)

        # Complexity Level
        self.complexity_var = tk.IntVar(value=1)
        options_menu.add_radiobutton(label="Low", variable=self.complexity_var, value=1, command=self.generate_password)
        options_menu.add_radiobutton(label="Medium", variable=self.complexity_var, value=2, command=self.generate_password)
        options_menu.add_radiobutton(label="High", variable=self.complexity_var, value=3, command=self.generate_password)

        options_menu.add_checkbutton(label="Include Uppercase Letters", variable=tk.BooleanVar(value=True), command=self.generate_password)
        options_menu.add_checkbutton(label="Include Digits", variable=tk.BooleanVar(value=True), command=self.generate_password)
        options_menu.add_checkbutton(label="Include Special Characters", variable=tk.BooleanVar(value=True), command=self.generate_password)

        # Password Length
        self.password_length_var = tk.StringVar(value=12)
        password_length_label = tk.Label(root, text="Password Length:", bg=bg_color, fg=label_color)
        password_length_label.pack(pady=5)
        password_length_entry = tk.Entry(root, textvariable=self.password_length_var)
        password_length_entry.pack(pady=5)

        # Password Display
        self.password_var = tk.StringVar()
        password_label = tk.Label(root, text="Generated Password:", bg=bg_color, fg=label_color)
        password_label.pack(pady=5)
        password_entry = tk.Entry(root, textvariable=self.password_var, state="readonly", width=30)
        password_entry.pack(pady=5)

        # Generate Password Button
        generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg=button_color, fg="white")
        generate_button.pack(pady=10)

    def generate_password(self):
        try:
            password_length = int(self.password_length_var.get())
            if password_length <= 0:
                messagebox.showinfo("Error", "Password length must be greater than zero.")
                return

            characters = string.ascii_lowercase

            if self.complexity_var.get() >= 2:
                characters += string.ascii_uppercase
            if self.complexity_var.get() >= 3:
                characters += string.digits + string.punctuation

            generated_password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_var.set(generated_password)
        except ValueError:
            messagebox.showinfo("Error", "Invalid password length. Please enter a valid number.")

    def save_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        self.root.update()
        messagebox.showinfo("Success", "Password saved to clipboard.")

    def save_to_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not file_path:
                return

            with open(file_path, "w") as file:
                file.write(self.password_var.get())

            messagebox.showinfo("Success", f"Password saved to {file_path}.")
        except Exception as e:
            messagebox.showinfo("Error", f"Error saving file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
