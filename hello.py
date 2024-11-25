import tkinter as tk 

root = tk.Tk()

root.title('Simple Button Function')
root.geometry("300x200")

def on_click_button():
    label.config(text='Button Clicked')

label = tk.Label(root, text='Click the button')
label.pack(pady=20)

button = tk.Button(root, text='Click me!', command=on_click_button)
button.pack(pady=20)

root.mainloop()