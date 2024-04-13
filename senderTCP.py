import tkinter as tk
import socket


def TcpMessage():
    try:
        message = entry.get()
        sent.send(message.encode('utf-8'))
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, sent.recv(1024).decode('utf-8'))
        text_widget.config(state=tk.DISABLED)
    except Exception as e:
        text_widget.insert(tk.END, f"Κενο Text :{e}")


root = tk.Tk()
root.title("TCP MESSAGES!")

HOST = 'Your Local IP'
PORT = The port of the server

sent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sent.connect((HOST, PORT))

name_label = tk.Label(root, text="Message: ")
name_label.pack()
entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="ΑΠΟΣΤΟΛΗ Μηνύματος", command=TcpMessage)
button.pack()

text_widget = tk.Text(root, height=10, width=50)
text_widget.pack()

root.mainloop()
