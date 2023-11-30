import numpy as np
import matplotlib.pyplot as plt

# Data nilai ujian mahasiswa
nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

# Menghitung rata-rata
rata_rata = np.mean(nilai_mahasiswa)

# Membuat diagram batang
plt.bar(range(len(nilai_mahasiswa)), nilai_mahasiswa, color='blue')
plt.axhline(rata_rata, color='red', linestyle='dashed', linewidth=2, label='Rata-rata')

# Menambahkan label pada sumbu x dan y
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')

# Menambahkan label pada diagram batang
for i, nilai in enumerate(nilai_mahasiswa):
    plt.text(i, nilai + 1, str(nilai), ha='center')

# Menampilkan rata-rata sebagai legenda
plt.legend()

# Menampilkan diagram batang
plt.show()