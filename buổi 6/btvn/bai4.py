num = int(input("Number of items: "))
item = []
medium = 0
for i in range(num):
   item_val = input(f'Item {i+1}: ')
   item.append(item_val)
   price_val = input(f'Price of item {i+1}: ')
   item.append(price_val)
for i in range(1, len(item), 2):
    medium += float(item[i])
medium = float(medium / (len(item)/2))
print(f"Average price: {medium}")
for i in range(1, len(item), 2):
    if float(item[i]) > medium:
        print(f"Item(s) above average price: {item[i-1]}, {item[i]}")
