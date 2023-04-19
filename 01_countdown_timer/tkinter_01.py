#
import tkinter as tk
from tkinter import messagebox

#
class CountdownTimer:

    #
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        # Create widgets and set all the properties needed for the widgets
        self.time_label = tk.Label(master, text="Enter time (in minutes):")
        self.time_entry = tk.Entry(master)
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.time_remaining = tk.Label(master, text="")
        self.quit_button = tk.Button(master, text="Quit", command=master.quit)

        # Layout widgets and set each columns and rows for the widget
        self.time_label.grid(row=0, column=0)
        self.time_entry.grid(row=0, column=1)
        self.start_button.grid(row=1, column=0)
        self.time_remaining.grid(row=1, column=1)
        self.quit_button.grid(row=2, column=1)

    #
    def start_timer(self):

        #
        try:

            # Getting the minutes values and multiplied by 60 which are the seconds per minutes
            time_remaining = (60 * int(self.time_entry.get()))

        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number.")
            return

        # In this while we set the magic of the decrease time by validating if the time remaining still greater than  zero.
        while time_remaining > 0:
            self.time_remaining.configure(text=f"Time remaining: {round((time_remaining / 60), 2)}")
            self.master.update()
            time_remaining -= 1
            self.master.after(1000) # Wait 1 second

        # send a message when the time's up.
        self.time_remaining.configure(text="Time's up!")

# Create the GUI window
root = tk.Tk()
root.geometry('500x200')
timer = CountdownTimer(root)
root.mainloop()
