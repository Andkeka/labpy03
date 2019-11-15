print("Program Menampilkan Bilangan Terbesar dari N Bilangan")

a = 1
max = 0
while a !=0:
    if a > max:
        max = a
    a = int(input("Masukan Bilangan:"))
    if a == 0:
        break
print("Nilai terbesar adalah:", max)