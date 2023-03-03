# NAMA: ADINDA APRILIANI 
# NIM: 2209116024
# KELAS: A SISTEM INFORMASI 2022

# Library
from numpy import random

# Variabel untuk tempat list kosong
mylist = []

# perulangan sebanyak 12 kali (angka acak yang dihasilkan sebanyak 12 angka)
for i in range(12):
    # Append untuk menambahkan angka ke dlm list kosong yg sdh disediakan
    mylist.append(random.randint(1, 80))

# Fungsi Mengurutkan data menggunakan Quick Sort
def quick_sort(urutan):
    if len(urutan) <= 1:
        return urutan
    else:
        pivot = urutan[0]

        # list Comprehensions (untuk mengecek, melakukan perulangan, mendeklarasikan nilai dalam array nya sendiri)
        kiri = [x for x in urutan[1:] if x <= pivot]  
        kanan = [x for x in urutan[1:] if x > pivot]
        
        # Return digunakan untuk mengembalikan nilai
        return quick_sort(kiri) + [pivot] + quick_sort(kanan)
    
# Run Program menghasilkan angka acak     
urutan = mylist
print(18*"=-=")
print(f"Sebelum di Sorting: {urutan}")
print(18*"=-=")

# Run Program mengurutkan data
hasil = quick_sort(urutan)
print(f"Setelah di sorting (Quick Sort): {hasil}")
print(18*"=-=")