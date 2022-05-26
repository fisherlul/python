n = int(input("Input a positive number: "))
fib = ""
def fibonacci(n):
    if (n < 0):
        print("Error, please enter a positive number")
    elif (n == 0 or n == 1):
        return n;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2);
for i in range(1, n+1):
    fib = fib + str(fibonacci(i)) + " ";
print(f"First 10 Fibonacci number(s): {fib}")
