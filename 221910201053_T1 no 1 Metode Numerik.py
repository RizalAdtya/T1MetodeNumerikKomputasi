import numpy as np
import matplotlib.pyplot as plt

# Data Input
data = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
g = 9.81
m = 68.1
c = 12.5
e = np.e
vt = 0

# Nilai array untuk menyimpan hasil
hasil = np.zeros_like(data, dtype=float)
hasil2 = np.zeros_like(data, dtype=float)

# solusi numerik
for i in range(1, len(data)):
    dt = data[i] - data[i - 1]
    vt_1 = vt + (g - ((c / m) * vt)) * dt
    hasil[i] = vt_1
    vt = vt_1

# solusi analitik
for i in range(1, len(data)):
    hasil2[i] = ((g * m) / c) * (1 - e ** (-(c / m) * data[i]))

 # Hasil nilai solusi numerik dan analitik 
    print (hasil[i])
    print (hasil2[i])
    print ("--")

# Plotting gambar hasil
plt.plot(data, hasil, label='Solusi Numerik')
plt.plot(data, hasil2, label='Solusi Analitik')
plt.xlabel('Waktu (s)')
plt.ylabel('Kecepatan (m/s)')
plt.title('Kecepatan vs Waktu')
plt.grid()
plt.legend()
plt.show()
