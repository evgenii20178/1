import tkinter as tk

class WordMover:
    def __init__(self, master):
        self.master = master
        self.master.title("Перекидыватель слов")
        
        self.word1 = tk.StringVar()
        self.word2 = tk.StringVar()
        
        self.entry1 = tk.Entry(self.master, textvariable=self.word1)
        self.entry1.grid(row=0, column=0, padx=10, pady=10)
        
        self.button = tk.Button(self.master, text="-->", command=self.move_word)
        self.button.grid(row=0, column=1, padx=10, pady=10)
        
        self.entry2 = tk.Entry(self.master, textvariable=self.word2)
        self.entry2.grid(row=0, column=2, padx=10, pady=10)
        
        self.direction = 1
        
    def move_word(self):
        if self.direction == 1:
            self.word2.set(self.word1.get())
            self.word1.set("")
            self.button.config(text="<--")
            self.direction = -1
        else:
            self.word1.set(self.word2.get())
            self.word2.set("")
            self.button.config(text="-->")
            self.direction = 1
        
if __name__ == "__main__":
    root = tk.Tk()
    app = WordMover(root)
    root.mainloop()