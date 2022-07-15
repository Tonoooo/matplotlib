# Invers dan Determinan

# penjelasan Perkalian Vektor (dot dan cross)
# atau link: https://youtu.be/gMQwec7NBVY

import numpy as np

a = np.array([(1,-1),(1,1)])

print(a)

# inverse matrix
print("~~~inverse matrix")
a_inv = np.linalg.inv(a)
print(a_inv)
print(np.dot(a,a_inv))

# determinan matrix
print("~~~determinan matrix")
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print(det_a)
print(det_a_inv)