import tkinter as tk
from tkinter import filedialog, messagebox


class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note")

        # Текущая тема
        self.dark_mode = False

        # Text area for writing notes
        self.text_area = tk.Text(self.root, wrap='word', font=("TT Ricordi Greto", 12))
        self.text_area.pack(expand=True, fill='both')

        # Menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="новый", command=self.new_note)
        file_menu.add_command(label="открыть", command=self.open_note)
        file_menu.add_command(label="сохранить", command=self.save_note)
        file_menu.add_command(label="сохранить как", command=self.save_as_note)
        file_menu.add_separator()
        file_menu.add_command(label="выйти", command=self.root.quit)

        # Меню для переключения тем
        view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Тема", menu=view_menu)
        view_menu.add_command(label="переключить тему", command=self.toggle_dark_mode)

    # Create a new note
    def new_note(self):
        self.text_area.delete(1.0, tk.END)

    # Open a note from file
    def open_note(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    # Save the note to the current file
    def save_note(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

    # Save the note with a specific name
    def save_as_note(self):
        self.save_note()

    # Функция для переключения между темами
    def toggle_dark_mode(self):
        if self.dark_mode:
            # Переключение на светлую тему
            self.text_area.config(bg="white", fg="black", insertbackground="black")
            self.menu_bar.config(bg="lightgrey", fg="black")
            self.dark_mode = False
        else:
            # Переключение на тёмную тему
            self.text_area.config(bg="black", fg="white", insertbackground="white")
            self.menu_bar.config(bg="black", fg="white")
            self.dark_mode = True

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.geometry("600x400")
    root.mainloop()
