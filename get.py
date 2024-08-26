import tkinter as tk
from tkinter import messagebox
import requests
import threading
import time
from urllib.parse import urlparse

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.successful_gets = 0
        self.errors = 0
        self.running = False

    def create_widgets(self):
        self.url_label = tk.Label(self)
        self.url_label["text"] = "URL:"
        self.url_label.pack(side="top")

        self.url_entry = tk.Entry(self)
        self.url_entry.pack(side="top")

        self.gets_label = tk.Label(self)
        self.gets_label["text"] = "Number of GETs:"
        self.gets_label.pack(side="top")

        self.gets_entry = tk.Entry(self)
        self.gets_entry.pack(side="top")

        self.delay_label = tk.Label(self)
        self.delay_label["text"] = "Delay (ms):"
        self.delay_label.pack(side="top")

        self.delay_entry = tk.Entry(self)
        self.delay_entry.pack(side="top")

        self.port_label = tk.Label(self)
        self.port_label["text"] = "Port (optional):"
        self.port_label.pack(side="top")

        self.port_entry = tk.Entry(self)
        self.port_entry.pack(side="top")

        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["command"] = self.start_gets
        self.start_button.pack(side="top")

        self.successful_gets_label = tk.Label(self)
        self.successful_gets_label["text"] = "Successful GETs: 0"
        self.successful_gets_label.pack(side="top")

        self.errors_label = tk.Label(self)
        self.errors_label["text"] = "Errors: 0"
        self.errors_label.pack(side="top")

        self.log_label = tk.Label(self)
        self.log_label["text"] = "Log:"
        self.log_label.pack(side="top")

        self.log_text = tk.Text(self, height=20, width=60)
        self.log_text.pack(side="top")
        self.log_text.config(state="disabled")

    def start_gets(self):
        if not self.running:
            self.running = True
            self.successful_gets = 0
            self.errors = 0
            self.successful_gets_label["text"] = "Successful GETs: 0"
            self.errors_label["text"] = "Errors: 0"
            self.log_text.config(state="normal")
            self.log_text.delete(1.0, tk.END)
            self.log_text.config(state="disabled")
            self.thread = threading.Thread(target=self.send_gets)
            self.thread.start()

    def send_gets(self):
        url = self.url_entry.get()
        num_gets = int(self.gets_entry.get())
        delay = int(self.delay_entry.get())
        port = self.port_entry.get()
        parsed_url = urlparse(url)
        ip = parsed_url.hostname
        if port:
            port = int(port)
        else:
            port = parsed_url.port if parsed_url.port else 80 if parsed_url.scheme == 'http' else 443

        for i in range(num_gets):
            try:
                # Construct the URL with the specified port
                if port:
                    url_with_port = f"{parsed_url.scheme}://{ip}:{port}{parsed_url.path}"
                else:
                    url_with_port = url

                response = requests.get(url_with_port)
                if response.status_code == 200:
                    self.successful_gets += 1
                    self.successful_gets_label["text"] = f"Successful GETs: {self.successful_gets}"
                    self.log(f"GET {url_with_port} successful ({response.status_code}) from {ip}:{port}")
                else:
                    self.errors += 1
                    self.errors_label["text"] = f"Errors: {self.errors}"
                    self.log(f"GET {url_with_port} failed ({response.status_code}) from {ip}:{port}")
            except requests.exceptions.RequestException as e:
                self.errors += 1
                self.errors_label["text"] = f"Errors: {self.errors}"
                self.log(f"GET {url_with_port} failed: {e} from {ip}:{port}")
            time.sleep(delay / 1000)
        self.running = False

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
