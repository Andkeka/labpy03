m = 100000000
sum = 0
y = 0
laba = [int(0), int(0), int(m) * 1, int (m) * 1, int(m) * 5, int(m) * 5, int(m) * 5, int(m) * 2]
print("Modal awal seorang pengusaha:", m)
for i in laba :
    sum = sum+i
    y+=1
    print("Laba Bulan ke-",y,"sebesar:", i)
print("Total laba adalah:",sum)