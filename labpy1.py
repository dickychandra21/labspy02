#!/usr/bin/phyton3
print("program menentukan bilangan terbesar dari 3 bilangan")
a = int(input("Masukkan nilai ke-1: "))
b = int(input("Masukkan nilai ke-2: "))
c = int(input("Masukkan nilai ke-3: "))

print("Dari bilangan ",a,b,c )

if a > b and a > c:
    print(a, "adalah nilai terbesar ")
elif b > a and b > c:
    print(b, "adalah nilai terbesar ")
else:
    print(c, "adalah nilai terbesar ")