import tkinter as tk
import time

class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.text = tk.Text(self.root)
        self.text.pack()
        self.start_button = tk.Button(self.root, text="Start", command=self.start_disappearing_text)
        self.start_button.pack()
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_disappearing_text)
        self.stop_button.pack()
        self.save_button = tk.Button(self.root, text="Save", command=self.save_text)
        self.save_button.pack()
        self.timer_running = False
        
    def start_disappearing_text(self):
        self.timer_running = True
        self.root.after(5000, self.delete_text)
        
    def delete_text(self):
        if self.timer_running:
            self.text.delete("1.0", tk.END)
        
    def stop_disappearing_text(self):
        self.timer_running = False
        
    def save_text(self):
        with open("text.txt", "w") as f:
            f.write(self.text.get("1.0", tk.END))

root = tk.Tk()
app = DisappearingTextApp(root)
root.mainloop()
