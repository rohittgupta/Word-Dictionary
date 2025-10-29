from tkinter import Tk
from gui.app import DictionaryApp

if __name__ == "__main__":
    root = Tk()
    root.title("Word Lookup Dictionary")
    app = DictionaryApp(root)
    root.mainloop()
