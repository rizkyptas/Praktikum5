import matplotlib.pyplot as plt

# Data transaksi penjualan produk dalam bentuk list tupel
transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk E", 70, 5)
]

# Ekstrak informasi dari tupel
produk, harga, jumlah_terjual = zip(*transaksi)

# Menghitung pendapatan produk
pendapatan = [harga[i] * jumlah_terjual[i] for i in range(len(harga))]

# Membuat scatter plot
plt.scatter(harga, jumlah_terjual, color='blue', marker='o', label='Hubungan Harga dan Jumlah Terjual')

# Menambahkan bar plot untuk menyajikan pendapatan produk
bar_width = 0.5
bar_positions = range(len(produk))
plt.bar(bar_positions, pendapatan, width=bar_width, color='green', alpha=0.7, label='Pendapatan Produk')

# Menambahkan label pada sumbu x dan y
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Terjual / Pendapatan')
plt.title('Scatter Plot dan Bar Plot Transaksi Penjualan Produk')

# Menambahkan label pada sumbu x untuk bar plot
plt.xticks(bar_positions, produk)

# Menambahkan legenda
plt.legend()

# Menampilkan scatter plot dan bar plot
plt.show()