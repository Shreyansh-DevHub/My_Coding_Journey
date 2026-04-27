import tkinter as tk
import webbrowser

w = tk.Tk()
w.title("My Window")    
w.geometry("400x300")


l = tk.Label(w, text="Hello, Tkinter!")
l.pack()


def click_button():
    webbrowser.open("https://github.com/Shreyansh-DevHub")

b = tk.Button(w, text="Click Me!", command=click_button)
b.pack()

w.mainloop()
