import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 180, 160, 175, 165, 185, 175, 170, 160]

# Menghitung frekuensi tinggi badan dalam interval tertentu
bins = [150, 160, 170, 180, 190]
hist, bin_edges = np.histogram(tinggi_badan, bins=bins)

# Membuat histogram
plt.bar(bin_edges[:-1], hist, width=10, alpha=0.7, color='blue', edgecolor='black')

# Membuat kurva PDF dari distribusi normal yang dihasilkan dari data tinggi badan
mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)

# Menambahkan label pada sumbu x dan y
plt.xlabel('Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram dan Kurva PDF Tinggi Badan')

# Menampilkan histogram dan kurva PDF
plt.show()