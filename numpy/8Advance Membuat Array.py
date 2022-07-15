# Cara Advance Membuat Array

# penjelasan Cara Advance Membuat Array
# atau link: https://youtu.be/Sa0a1G71MBA

import numpy as np

#1. membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype = float)

#2. membuat array menggunakan function
def kuadrat(baris,kolom):
    return kolom**2

def jumlah(baris,kolom):
    return (kolom + baris)

 # caranya np.formfanction(nama fungsi, ukuran matrix,tipe data)
b = np.fromfunction(kuadrat, (1,10), dtype=int)
c = np.fromfunction(jumlah, (4,4), dtype=float)

#3. membuat array/matrix dengan menggunakan iterable
iniiterable = (x*x for x in range(5)) # x nya di kuadratkan untuk setiap x yang ada di range 0 sampai 5
inijugaiterable = (x*2 for x in range(5)) # x nya di kali 2 untuk setiap x yang ada di range 0 sampai 5

d = np.fromiter(iniiterable,dtype=int)
dd = np.fromiter(inijugaiterable,dtype=int)

#4. multitype array = array yang isinya bukan cuma angka

dtipee = [('nama','S255'),('tinggi',int)] # ('nama','S255'),('tinggi',int) ini seperti argumen difungsi dana S255 = s artinya string dan 255 adalah batasnya sampai 255(bebas sihh batas nya mauberapaaja)
data = [
    ('tono',150),
    ('suep',160),
    ('adom',170)
]

e = np.array(data,dtype=dtipee) # nanti hasilnya ada b'tono' artinya tono type datanya byte

print(e)
print(e[0]) # [0] melihat yang pertama