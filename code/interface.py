import tkinter as tk

def make_window(connect, send):
    window = tk.Tk()
    window.resizable(False, False)
    window.title("Main Window")
    window.geometry("719x357")

    text = tk.Text(
        window,
        width=63,   # roughly approximate 448px
        height=18,  # roughly approximate 214px
        bg="#343739",   # background color
        fg="#ffffff",   # text color
        font=("Arial", 16),
        cursor="cross"  # cursor style
    )
    text.place(x=135, y=17)

    text.insert("end", "مرحبا! هذا حقل نص يدعم العربية.\nيمكنك الكتابة هنا.\n")

    bar = tk.Frame(window, width=700, height=2, bg="#A6192E")
    bar.pack(pady=9)

    connect_btn = tk.Button(window, text="Connect", command=lambda: connect(), width=9)
    connect_btn.place(x=10, y=20)

    send_btn = tk.Button(window, text="Send", command=lambda: send(), width=9)
    send_btn.place(x=10, y=70)

    elements = {
        "window": window, 
        "text": text, 
        "bar": bar, 
        "connect_btn": connect_btn, 
        "send_btn": send_btn, 
        "status": False
    }
    return elements

def update_connection_status(whatsapp, elements):
    if whatsapp.loggedIn() and whatsapp.isConnected():
        elements["bar"].configure(bg="#4cae4f")
        elements["status"] = True
    else:
        elements["bar"].configure(bg="#A6192E")
        elements["status"] = False
    elements["window"].after(5000, update_connection_status(whatsapp, elements))



# btn_green.pack(pady=5)

# btn_red = tk.Button(window, text="Set Red", command=lambda: set_red(bar))
# btn_red.pack(pady=5)



# import os
# import customtkinter as ctk

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
