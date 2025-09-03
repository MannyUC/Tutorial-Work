# A simple function
def greet(name):
    # Return a friendly greeting:
    return f"Hello, {name}!"

# Using the function
message = greet("Aisha")
print(message)  # Hello, Aisha!

def area_of_rectangle(width, height):
    return width * height

print(area_of_rectangle(3, 5))   # 15


def power(base, exponent=2):
    return base ** exponent

print(power(5))          # 25 (uses default exponent=2)
print(power(2, exponent=3))  # 8 (keyword argument)


PI = 3.14159  # global variable

def circle_area(r):
    "Compute area of a circle of radius r."
    return PI * (r ** 2)

print(circle_area(2))  # 12.56...

#1.Fahrenheit Function 
def fahrenheit_to_celsius(f):
    return (f-32) * 5/9

#2.Even Function
def is_even(n):
    even= n % 2
    if even==0:
        print("True")
    else:
        print("False")
        

#3 Triangle Area
def triangle_area(b,h=1):
    return 0.5*h*b

#Part B

count = 0
def add():
    global count 
    count += 1
    label.config(text=str(count)) 
    
import tkinter as tk

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root,text="0", font=("Arial", 18))
label.pack(pady=10)

tk.Button(root, text="Add 1",command=add).pack(pady=6) 

root.mainloop()
