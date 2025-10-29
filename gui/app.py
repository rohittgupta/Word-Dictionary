import tkinter as tk
from core.dictionary import Dictionary

class DictionaryApp:
    def __init__(self, root):
        self.dictionary = Dictionary()

        self.entry = tk.Entry(root, width=40, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.search_btn = tk.Button(root, text="Search", command=self.lookup, font=("Arial", 12))
        self.search_btn.pack()

        self.result = tk.Text(root, height=10, width=60, font=("Arial", 12))
        self.result.pack(pady=10)

    def lookup(self):
        word = self.entry.get().strip()
        res = self.dictionary.lookup(word)
        self.result.delete(1.0, tk.END)

        if "word" in res:
            self.result.insert(tk.END, f"{res['word']} → {res['definition']}\n")
        elif "suggestions" in res:
            self.result.insert(tk.END, f"Suggestions: {', '.join(res['suggestions'])}\n")
        elif "corrections" in res:
            self.result.insert(tk.END, f"Did you mean: {', '.join(res['corrections'])}?\n")
        else:
            self.result.insert(tk.END, "No results found.")
