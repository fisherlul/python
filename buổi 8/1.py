def is_int(num):
    if num == int(num):
        return True
    else:
        return False 

num = float(input('Input number: '))
if is_int(num):
    print(f'{num} is an integer')
else:
    print(f'{num} is not an integer')
