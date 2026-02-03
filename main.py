# VLESS Xray Application for Windows 11

import os
import sys
import time
from tkinter import *
from tkinter import messagebox

class VLESSApp:
    def __init__(self, master):
        self.master = master
        self.master.title("VLESS Xray Application")
        self.mode = StringVar(value='VPN')  # Default mode

        self.create_widgets()

    def create_widgets(self):
        # Mode Selection
        Label(self.master, text="Select Mode:").pack(pady=10)
        Radiobutton(self.master, text='VPN', variable=self.mode, value='VPN', command=self.mode_changed).pack(anchor=W)
        Radiobutton(self.master, text='Proxy', variable=self.mode, value='Proxy', command=self.mode_changed).pack(anchor=W)

        # Start Button
        self.start_button = Button(self.master, text='Start', command=self.start_application)
        self.start_button.pack(pady=20)

        # Status Label
        self.status_label = Label(self.master, text='Status: Ready')
        self.status_label.pack(pady=10)

    def mode_changed(self):
        self.status_label.config(text=f'Status: Mode changed to {self.mode.get()}')

    def start_application(self):
        mode = self.mode.get()
        self.status_label.config(text=f'Status: Starting {mode} mode...')
        
        # Simulate starting the application
        time.sleep(2)  # Simulating delay

        self.status_label.config(text=f'Status: {mode} mode running!')
        messagebox.showinfo("Info", f"{mode} mode started!")

if __name__ == '__main__':
    root = Tk()
    app = VLESSApp(root)
    root.geometry('300x200')
    root.mainloop()