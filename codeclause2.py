import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")

        self.word_list = [
            "python", "programming", "challenge", "typing", "practice", "speed",
            "keyboard", "algorithm", "developer", "coding", "language", "text",
            "race", "accuracy", "learn", "fun", "coding", "skill", "test"
        ]

        self.current_word = tk.StringVar()
        self.input_word = tk.StringVar()
        self.time_left = tk.StringVar()
        self.score = tk.IntVar()

        self.time_limit = 60
        self.score.set(0)
        self.is_running = False

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.root, textvariable=self.current_word, font=("Helvetica", 24))
        self.word_label.pack(pady=20)

        self.entry = tk.Entry(self.root, textvariable=self.input_word, font=("Helvetica", 20))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_word)

        self.timer_label = tk.Label(self.root, textvariable=self.time_left, font=("Helvetica", 18))
        self.timer_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score:", font=("Helvetica", 18))
        self.score_label.pack()
        self.score_display = tk.Label(self.root, textvariable=self.score, font=("Helvetica", 24))
        self.score_display.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_game, font=("Helvetica", 18))
        self.start_button.pack()

    def start_game(self):
        if not self.is_running:
            self.is_running = True
            self.input_word.set("")
            self.current_word.set(random.choice(self.word_list))
            self.score.set(0)
            self.update_timer(self.time_limit)
            self.entry.config(state="normal")
            self.start_button.config(state="disabled")
            self.entry.focus_set()

    def check_word(self, event):
        if self.is_running:
            input_text = self.input_word.get().strip()
            current_text = self.current_word.get()

            if input_text == current_text:
                self.score.set(self.score.get() + 1)
                self.input_word.set("")
                self.current_word.set(random.choice(self.word_list))

    def update_timer(self, time_left):
        if self.is_running:
            self.time_left.set("Time Left: {}s".format(time_left))
            if time_left > 0:
                self.root.after(1000, self.update_timer, time_left - 1)
            else:
                self.end_game()

    def end_game(self):
        self.is_running = False
        self.entry.config(state="disabled")
        self.start_button.config(state="normal")
        self.input_word.set("")
        self.current_word.set("Game Over!")
        messagebox.showinfo("Game Over", "Your Score: {}".format(self.score.get()))

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTypingTest(root)
    root.mainloop()
