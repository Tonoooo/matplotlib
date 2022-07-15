# Solusi Persamaan Linear

# penjelasan Solusi Persamaan Linear
# atau link: https://youtu.be/6cfuKThXoVc

import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array([23,14])

print(A)
print(Y)

A_inv = np.linalg.inv(A)

# menyelesaikan permasalahan linear
X = np.dot(A_inv,Y)
print(X)

# cara lain. kita tidak perlu menginvers lagi
X2 = np.linalg.solve(A,Y) # solve = numpy sudah ada perkalian seperti diatas
print(X2)