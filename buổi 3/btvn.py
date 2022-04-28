import turtle as t
#bai1
num = int(input("Enter number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#bai2
num = float(input("Input number: "))
if num == int(num):
    print(f"{num} is an integer")
else:
    print(f"{num} is not an integer")

#bai3
char = input("Input character: ")
if char>="0" and char<="9":
    print(f"{char} is a digit")
else:
    print(f"{char} is not a digit")

#bai4
n = int(input("Input number: "))
if n%3 == 0 and n%5 == 0:
    print(f"{n} is divisible by 3 and 5")
elif n%3 == 0 and n%5 != 0:
    print(f"{n} is divisible by 3")
elif n%3 != 0 and n%5 == 0:
    print(f"{n} is divisible by 5")
else:
    print(f"{n} is not divisible by 3 nor by 5")

#bai5
username_def = "admin"
password_def = "12345"
username = input("Username: ")
password = input("Password: ")
if username == username_def and password == password_def:
    print("You are logged in, admin.")
else:
    print("Wrong username or password.")

#bai6
l1 = float(input("Input length 1: "))
l2 = float(input("Input length 2: "))
l3 = float(input("Input length 3: "))
if l1+l2 > l3 or l2+l3>l1 or l1+l3 >l2:
    print("The 3 line segments can form a triangle")
else:
    print("The 3 line segments cannot form a triangle")

#bai7
l1 = float(input("Input length 1: "))
l2 = float(input("Input length 2: "))
l3 = float(input("Input length 3: "))
if l1+l2 > l3 or l2+l3>l1 or l1+l3 >l2:
    if (l1**2 + l2**2 == l3**2) or (l3**2 + l2**2 == l1**2) or (l1**2 + l3**2 == l2**2):
        print("The 3 line segments can form a right triangle")
    elif l1==l2==l3:
        for i in range(3):
            t.forward(l1*30)
            t.left(120)
    else:
        print("The 3 line segments can form a triangle")
else:
    print("The 3 line segments cannot form a triangle")