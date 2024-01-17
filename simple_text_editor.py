import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Editor Py")
        self.text_area = tk.Text(self.window, wrap=tk.WORD)
        self.text_area.pack(expand=tk.YES, fill=tk.BOTH)
        self.create_menu()
        self.window.mainloop()

    def create_menu(self):
        menu = tk.Menu(self.window)
        self.window.config(menu=menu)
        menu.add_command(label="New", command=self.new_file)
        menu.add_command(label="Open", command=self.open_file)
        menu.add_command(label="Save", command=self.save_file)
        menu.add_separator()
        menu.add_command(label="Exit", command=self.window.quit)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
        if file:
            self.window.title(f"Python Text Editor - {file}")
            self.text_area.delete(1.0, tk.END)
            with open(file, 'r') as file_handler:
                self.text_area.insert(tk.INSERT, file_handler.read())

    def save_file(self):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
        if file:
            with open(file.name, "w") as file_handler:
                file_handler.write(self.text_area.get(1.0, tk.END))
            self.window.title(f"Python Text Editor - {file}")

if __name__ == "__main__":
    text_editor = TextEditor()
