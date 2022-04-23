dep = float(input("Enter deposit: "))
year = int(input("Enter year: "))
acc = dep * (1.05)**year
print(f'Account after {year} year(s): {acc}')
