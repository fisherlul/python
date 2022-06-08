def factorial(n):
    fact = 1;
    if (n == 0 or n == 1):
        return fact
    else:
        for i in range(2, n + 1):
            fact *= i
        return fact

n = int(input("Input number: "))
result = 0
for i in range(1, n + 1):
    result += factorial(i)/i 
print(f'Result: {int(result)}')