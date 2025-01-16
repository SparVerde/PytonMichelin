import tkinter as tk

window = tk.Tk() #we create an object on class
print(window)

window.winfo_screenwidth()
#another function geometry
width=height=600
x=100
y=150
window.geometry(f'{width}x{height}+{x}+{y}')



window.mainloop()