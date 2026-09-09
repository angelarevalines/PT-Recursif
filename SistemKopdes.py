# import ini jangan dihapus/diedit yak
import random


def totalPenjualan(namaBarang,penjualan):
    # kerjakan di sini
    if penjualan == 0:
        return 0
    return namaBarang [penjualan - 1][1]+ totalPenjualan(namaBarang,penjualan - 1)
        


def penjualanTertinggi(data, n):
    if n == 1:
        return data[0]
    
    tertinggi_sebelumnya = penjualanTertinggi(data, n - 1)
    
    if data[n - 1][1] > tertinggi_sebelumnya[1]:
        return data[n - 1]
    else:
        return tertinggi_sebelumnya

def diAtasRataRata(penjualan, rataRata):
    
    jumlah_di_atas = 0
    for nilai in penjualan.values():
        if nilai > rataRata:
            jumlah_di_atas += 1
    return jumlah_di_atas


# Program Utama - Jangan dihapus/diedit yak
angka = int(input("NIM: "))
random.seed(angka)

barang = [
    "Beras",
    "Minyak",
    "Gula",
    "Telur",
    "Kopi",
    "Teh"
]

penjualan = {}

for namaBarang in barang:
    penjualan[namaBarang] = random.randint(100, 500)

data = list(penjualan.items())
n = len(data)

print("\n===== Data Penjualan =====")
for namaBarang, jumlah in penjualan.items():
    print(namaBarang, ":", jumlah)

total = totalPenjualan(data, n)
tertinggi = penjualanTertinggi(data, n)
rataRata = total / n
jumlahDiAtasRataRata = diAtasRataRata(penjualan, rataRata)

print("\n===== Hasil Analisis =====")
print("Total penjualan        :", total)
print("Penjualan tertinggi    :", tertinggi[0], "(", tertinggi[1], ")")
print("Rata-rata penjualan    :", round(rataRata, 2))
print("Di atas rata-rata      :", jumlahDiAtasRataRata, "barang")