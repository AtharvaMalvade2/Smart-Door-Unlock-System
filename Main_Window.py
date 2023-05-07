import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webbrowser
import tkinter.font as TkFont
from ttkbootstrap import Style


window = tk.Tk()
window.geometry("2160x840")
# window.attributes('-fullscreen', True)


def openlink():
    webbrowser.open("facelook.py")


s = ttk.Style()
s.configure('.', font=('Times', 16))

font = TkFont.Font(family="Arial", size=40, weight="bold", underline=1)

ttk.Label(window, text="🚪 Smart Door Unlock System 🔓", padding=50,
          font=font).pack()

f1 = TkFont.Font(family="Courier", size=32, weight="bold")

b1 = ttk.Button(window, text="Click to Unlock the door \n   by scanning your face \n                   🔍",
                bootstyle="outline", command=openlink, cursor="	hand2")

b1.pack(ipadx=5, ipady=20, padx=20, pady=110)


def samplelink():
    webbrowser.open("collectingdata.py")


b2 = ttk.Button(window, text="Click to collect face samples",
                bootstyle=(INFO, OUTLINE), command=samplelink, cursor="dotbox")
b2.pack(ipadx=5, ipady=20, padx=20, pady=10)

window.configure(bg='#F7E8F9')
window.mainloop()


# # Create a string.
# linkbutton = ttk.Button(window, text="Click to Unlock the door", command=openlink,height=3, width=40,fg ='red', bg='white')
# linkbutton2 = Button(window, text="Click to collect face samples", command=samplelink, height=3, width=40)
# linkbutton.pack(padx=4, pady=10)
# linkbutton2.pack(padx=4, pady=10)
