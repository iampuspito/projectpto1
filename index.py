print('## Program Python Penjumlahan Array PTO ##')
print('======================================')
print()

n = int(input('Input Jumlah Elemen List: '))
print()

print('Input',n,'angka (dipisah dengan enter): ');

x = []
for i in range(n):
    print('Angka ke-',i+1,': ',sep='',end='')
    x.append(int(input()))

print()
total = sum(x)

print('Total penjumlahan dari',n,'angka tersebut adalah: ',total);