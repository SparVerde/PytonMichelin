import tkinter as tk

window = tk.Tk()
print(window)

SCREEN_WIDTH = window.winfo_screenwidth()
SCREEN_HEIGHT = window.winfo_screenheight()

width = height = 600
x = SCREEN_WIDTH // 2 - width // 2
y = SCREEN_HEIGHT // 2 - height // 2
window.geometry(f"{width}x{height}+{x}+{y}")



label = tk.Label(window, text="Two more days of fun")
label.pack()

label_2 = tk.Label(window, text="what a great days")
label_2.pack()


counter = 0

def count():   
    global counter  
    print("The button was pushed")
    counter += 1
    print(f"You pushed for {counter} times")

button = tk.Button(window, text="Push me", command=count)
button.pack()

window.mainloop()