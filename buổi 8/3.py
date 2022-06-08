def is_prime(num) -> bool:
    if (num < 2):
        return False
    for i in range(2, num-1):
        if (num % i == 0):
            return False
    return True

n = int(input('Input number of prime numbers: '))
dem = 0
i = 2
print(f"First {n} prime(s):", end = ' ')
while (dem < n):
    if (is_prime(i)): 
        print(i, end = ' ')
        dem += 1
    i += 1
