import tkinter as tk
import time
import sqlite3
import subprocess

def db_setup():
    subprocess(["python3", "words.py"])

class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Typing Game")
        self.root.geometry("400x300")
        
        self.score = 0
        self.time_limit = 30
        self.start_time = None
        self.used_words = []
        self.current_word = self.get_random_word()
        
        self.instructions = tk.Label(root, text="Type the word shown below as quickly as possible.")
        self.instructions.pack(pady=10)
        
        self.word_label = tk.Label(root, text=self.current_word, font=('Formal Script', 24))
        self.word_label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=('Formal Script', 14))
        self.entry.pack()
        self.entry.bind("<Return>", self.check_word)
        self.entry.config(state="disabled")
        
        self.timer_label = tk.Label(root, text="Time left: 30", font=('Formal Script', 12))
        self.timer_label.pack(pady=20)
  
        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

    def get_random_word(self):
        conn = sqlite3.connect('words.db')  
        cursor = conn.cursor()

        if self.used_words:
                placeholders = ','.join('?' for _ in self.used_words)
                query = f'SELECT word FROM words WHERE word NOT IN ({placeholders}) ORDER BY RANDOM() LIMIT 1'
                cursor.execute(query, self.used_words)
        else:
            cursor.execute('SELECT word FROM words ORDER BY RANDOM() LIMIT 1')        
            
        word = cursor.fetchone()
        
        conn.close()
        return word[0] if word else None

    def start_game(self):
        self.score = 0
        self.start_time = time.time()
        self.update_timer()
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.start_button.config(state="disabled")  

    def check_word(self, event):
        user_input = self.entry.get().strip()
        if user_input == self.current_word:
            self.score += 1
            self.used_words.append(self.current_word) 
            self.entry.delete(0, tk.END)
            self.current_word = self.get_random_word()
            self.word_label.config(text=self.current_word)
        if self.current_word is None:
            self.end_game()
    def update_timer(self):
        time_left = self.time_limit - int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time left: {time_left}")
        
        if time_left > 0:
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        self.entry.config(state="disabled") 
        wpm = self.score * 2
        self.timer_label.config(text=f"Time's up! Your WPM is: {wpm}")
        self.start_button.config(state="normal")  

root = tk.Tk()
app = TypingGame(root)
root.mainloop()

if __name__ == "__main__":
    db_setup()