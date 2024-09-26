import tkinter as tk

class SimpleGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple GUI")

        # Label and Entry fields
        tk.Label(self.window, text="Enter your name:").grid(row=0)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1)

        # Button to greet user
        tk.Button(self.window, text="Greet Me", command=self.greet_user).grid(row=2, column=1)

        # Label to display greeting message
        self.greeting_label = tk.Label(self.window, text="")
        self.greeting_label.grid(row=3)

    def greet_user(self):
        name = self.name_entry.get()
        greeting_message = f"Greeting's, {name}!"
        self.greeting_label['text'] = greeting_message

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = SimpleGUI()
    gui.run()