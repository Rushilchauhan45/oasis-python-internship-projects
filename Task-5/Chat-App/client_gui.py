import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk

# ----------------- Network Setup -----------------
nickname = input("Enter your nickname: ")
host = '127.0.0.1'
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((host, port))
except:
    print("Unable to connect to the server")
    exit()

# ----------------- GUI Setup -----------------
window = tk.Tk()
window.title(f"Chat - {nickname}")
window.geometry("500x600")
window.configure(bg="#1e1e2f")  # Dark futuristic background
window.resizable(False, False)

# ----------------- Chat Area Frame -----------------
chat_frame = tk.Frame(window, bg="#2b2b3f", bd=2, relief=tk.RIDGE)
chat_frame.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, bg="#1e1e2f",
                                      fg="#f0f0f0", font=("Segoe UI", 11), relief=tk.FLAT)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.config(state='disabled')

# ----------------- Entry Frame -----------------
entry_frame = tk.Frame(window, bg="#1e1e2f")
entry_frame.pack(padx=15, pady=(0, 15), fill=tk.X)

message_entry = tk.Entry(entry_frame, font=("Segoe UI", 12), bg="#2b2b3f", fg="#ffffff",
                         insertbackground='white', relief=tk.FLAT)
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,10), ipady=6)

# Gradient-like 3D Send Button
send_button = tk.Button(entry_frame, text="Send", command=lambda: send_message(),
                        bg="#ff4c4c", fg="#ffffff", font=("Segoe UI Bold", 12),
                        activebackground="#ff1a1a", relief=tk.RAISED, bd=4)
send_button.pack(side=tk.RIGHT)

# Add hover effect for send button
def on_enter(e):
    send_button['bg'] = "#ff1a1a"
def on_leave(e):
    send_button['bg'] = "#ff4c4c"

send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

# ----------------- Send Message Function -----------------
def send_message():
    message = message_entry.get()
    if message:
        full_message = f"{nickname}: {message}"
        client.send(full_message.encode('utf-8'))
        message_entry.delete(0, tk.END)

# ----------------- Receive Messages -----------------
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                chat_area.config(state='normal')
                chat_area.insert(tk.END, message + "\n")
                chat_area.yview(tk.END)
                chat_area.config(state='disabled')
        except:
            messagebox.showerror("Error", "Connection lost")
            client.close()
            break

# Start receiving thread
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

# ----------------- Enter key sends message -----------------
message_entry.bind("<Return>", lambda event: send_message())

# Start GUI
window.mainloop()