import tkinter as tk
from file_manager import FileManager

class ButtonController:

    def __init__(self, fenster, textfeld, file_manager):
        self.fenster = fenster
        self.textfeld = textfeld
        self.file_manager = file_manager
        
        # Buttons hinzufügen
        self.speichern_button = tk.Button(fenster, text="Speichern", command=self.speichern)
        self.speichern_button.pack(side=tk.LEFT, padx=10)

        self.laden_button = tk.Button(fenster, text="Laden", command=self.laden)
        self.laden_button.pack(side=tk.LEFT, padx=10)

    def speichern(self):
        self.file_manager.speichern(self.textfeld)

    def laden(self):
        self.file_manager.laden(self.textfeld)
