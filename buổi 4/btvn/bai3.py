n = int(input("Input number: "))
fact = 1
if n < 0:
    print("Invalid")
else:
    for i in range(1, n+1):
        if i == 0:
            print(f"{i}! = 1")
        else:
            fact *= i
print(fact)