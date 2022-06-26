numbers = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5,
'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10}
x = numbers.get(input('Input a Roman number: '))
if x == None:
    print("Not found.")
else:
    print(x)