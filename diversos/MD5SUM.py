import tkinter as tk
import hashlib
from tkinter import filedialog

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Selecionar arquivo"
        self.select_button["command"] = self.select_file
        self.select_button.pack(side="top")

        self.filename_label = tk.Label(self)
        self.filename_label["text"] = ""
        self.filename_label.pack(side="top")

        self.hash_button = tk.Button(self)
        self.hash_button["text"] = "Gerar soma MD5"
        self.hash_button["command"] = self.generate_md5
        self.hash_button.pack(side="top")

        self.hash_label = tk.Label(self)
        self.hash_label["text"] = ""
        self.hash_label.pack(side="top")

        self.quit_button = tk.Button(self, text="Sair", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")

    def select_file(self):
        self.filename = filedialog.askopenfilename()
        self.filename_label.config(text=self.filename)

    def generate_md5(self):
        try:
            with open(self.filename, "rb") as f:
                file_contents = f.read()
                hash_object = hashlib.md5(file_contents)
                md5_sum = hash_object.hexdigest()
                self.hash_label.config(text="Soma MD5: " + md5_sum)
        except Exception as e:
            self.hash_label.config(text="Erro ao gerar soma MD5: " + str(e))

root = tk.Tk()
app = App(master=root)
app.mainloop()
