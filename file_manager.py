import tkinter as tk
from tkinter import filedialog

class FileManager:
    def speichern(self, textfeld):
        datei = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
        if datei:
            with open(datei, 'w', encoding='utf-8') as f:
                f.write(textfeld.get("1.0", tk.END))

    def laden(self, textfeld):
        datei = filedialog.askopenfilename(filetypes=[("Textdateien", "*.txt")])
        if datei:
            with open(datei, 'r', encoding='utf-8') as f:
                textfeld.delete("1.0", tk.END)
                textfeld.insert(tk.END, f.read())
