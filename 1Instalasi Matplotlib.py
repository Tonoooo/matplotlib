import numpy as np
import matplotlib.pyplot as plt # dipakeg matplotlib ada modul pyplot

# membuat lingkaran
PI = np.pi  # pi itu adalah 3,14
sudut = np.linspace(0,2*PI,100)
radius = 5  #ini diameter lingkaran

x = radius * np.cos(sudut)
y = radius * np.sin(sudut)

# inisialisasi plot = memberi nilai pada plotnya
plt.plot(x,y)

# tampilkan
plt.show()
