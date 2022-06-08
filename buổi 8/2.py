def is_prime(num) -> bool:
    if (num < 2):
        return False
    for i in range(2, num-1):
        if (num % i == 0):
            return False
    return True

num = int(input('Input number: '))
if is_prime(num):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
    

