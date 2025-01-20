import tkinter as tk
from tkinter import filedialog

class MeineGui:
    def __init__(self,fenster):
        fenster.title("Editor")
        fenster.geometry("1200x600")
        fenster.resizable(False,False)

        self.aktuelle_datei = ""
# menubar erstellen
        menubar = tk.Menu(fenster)
        fenster.config(menu=menubar)

        datemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Datei", menu=datemenu) #hierwird dein Menüpunkt Datei erstellt

        dateimenue.add_command(label="neu")
        dateimenue.add_command(label="öffnen")
        dateimenue.add_command(label="neu")
root = tk.Tk()
app = MeineGui(root)
root.mainloop()
