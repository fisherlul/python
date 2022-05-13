n = int(input("Nhập số nguyên dương n = "))
total = 0
while (n > 0):
    total = total + n % 10
    n = int(n / 10)
print("Tổng các chữ số của", n, "là", total)