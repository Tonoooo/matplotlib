# Set Axis
# axis adalah  seperti garis x dan garis y

import numpy as np
import matplotlib.pyplot as plt

# membuat data(sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):  # nama fungsi ini disebut cemal case (huruf kecil dikataawal dan kata berikutnya diawali huruf besar). kalo memberi nama class harus diawali huruf besar
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0)

# membuat plot
plt.plot(t,y)

# setting axis minimum sama maximum
 # caranya: plt.axis([xmin,xmax,ymin,ymax])
plt.axis([0,4,-1,1])

# menampilkan
plt.show()