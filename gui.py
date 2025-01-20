import re
import tkinter as tk
from file_manager import FileManager
from button_controller import ButtonController

class TextEditorGUI:
    def __init__(self):
        self.fenster = tk.Tk()
        self.fenster.title("Einfacher Texteditor")
        
        self.textfeld = tk.Text(self.fenster, wrap="word", height=20, width=60)
        self.textfeld.pack(padx=10, pady=10)
        
        self.textfeld.bind("<KeyRelease>", self.highlight_syntax)  # Event für Tastatureingabe
        
        self.file_manager = FileManager()
        self.button_controller = ButtonController(self.fenster, self.textfeld, self.file_manager)
        
        # Tags für Syntax Highlighting definieren
        self.textfeld.tag_configure("keyword", foreground="blue")
        self.textfeld.tag_configure("string", foreground="green")
        self.textfeld.tag_configure("comment", foreground="gray")
    
    def start(self):
        self.fenster.mainloop()
    
    def highlight_syntax(self, event=None):
        text = self.textfeld.get("1.0", tk.END)
        self.textfeld.mark_set("range_start", "1.0")
        self.textfeld.mark_set("range_end", "1.0")
        
        # Schlüsselwörter und Regex für Highlighting
        keywords = ["if", "else", "for", "while", "def", "class"]
        patterns = {
            "keyword": r"\b(?:{})\b".format("|".join(keywords)),  # Wörter wie 'if', 'else' etc.
            "string": r"\"(.*?)\"|\'(.*?)\'",  # Strings in Anführungszeichen
            "comment": r"#[^\n]*"  # Kommentare (alles nach '#')
        }

        # Anwenden der Formatierungen
        for tag, pattern in patterns.items():
            self.apply_tag(tag, pattern, text)

    def apply_tag(self, tag, pattern, text):
        for match in re.finditer(pattern, text):
            self.textfeld.tag_add(tag, match.start(), match.end())
