# Perkalian Vektor (dot dan cross)

# penjelasan Perkalian Vektor (dot dan cross)
# atau link: https://youtu.be/taHnC0WHXB8

import numpy as np

a = np.array([1,3])
b = np.array([2,1])

# perkalian dot
c = np.dot(a,b)

# perkalian cross
aa = np.array([1,2,0])
bb = np.array([2,1,0])

cc = np.cross(aa,bb)
c3 = np.cross(bb,aa)
print(c3)