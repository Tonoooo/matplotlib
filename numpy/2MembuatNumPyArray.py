### Membuat NumPy Array
# Secara umum, array satu dimensi dengan vector jika dilihat secara sepintas terlihat sangat mirip dan susah untuk dibedakan
# sehingga tidak jarang banyak orang yang menyebut bahwa vector adalah array satu dimensi, sedangkan array dua dimensi adalah
# matrix. Ternyata yang membedakan antara vector dan array adalah array dapat dilakukan proses transpose, sedangkan vector tidak
# dapat di-transpose.

# Matriks adalah susunan angka-angka dalam bentuk bujur sangkar atau persegi panjang yang diapit 
# oleh tanda kurung. Semua bilangan yang ada dalam matriks adalah bilangan real. ... 
# Vektor adalah matriks yang hanya memiliki satu kolom saja atau hanya memiliki satu baris saja.

import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5 , 2.5 , 5, 6, 7]) #ini nampilkan koma
# membuat vector dengan range
c = np.arange(1,10,2) # dimulai dari satu, berakhir sebelum 10, dengan step/loncat/jarak 2
# membuat linspace
d = np.linspace(1,10,4) # i sampai 10 tapi terbagi 4 bagian (nampilin 4 angka didalam range 1 sampai 10 dengan jarak yg sama)
# array multidimensi / matrix
e = np.array([ (1,2,3) , (4,5,6)]) # artinya (1,2,3) baris kesatu, (4,5,6) baris kedua

# matrix dengan nilai nol
f = np.zeros((5,5)) # artinya 5 kali 5 maksudnya 5 kolom 5 baris
ff = np.zeros(5) # komponennya ada 5

# matrix dengan nilai 1
g = np.ones(5) # komponennya ada 5
gg = np.ones((5,5)) # artinya 5 kali 5 maksudnya 5 kolom 5 baris

# matrix identitas(ini berguna untuk AI) = komponennya 0 tapi diagonalnya 1
h = np.identity(5) # kolom dan baris nya sama 5
hh = np.eye(5) # sama aja

# display
print(hh)