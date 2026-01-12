
from tkinter import *

window = Tk()

window.title("product")
window.geometry("400x300")

num1 = Label(text = "enter first number:_")
num2 = Label(text = "enter second number:_")

num1_entry = Entry()
num2_entry = Entry()

def calculate():
    a = num1_entry.get()
    b = num2_entry.get()
    product = int(a) * int(b)
    result = "the product is :- ",  product
    text_box.insert(END,result)
text_box = Text(height=1)

btn = Button(text="start calculate", command = calculate)

num1.pack()
num1_entry.pack()
num2.pack()
num2_entry.pack()
btn.pack()
text_box.pack()
window.mainloop()

