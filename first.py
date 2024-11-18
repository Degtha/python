def operasi ():
    angka1 = int(input("MASUKKAN ANGKA PERTAMA :"))
    angka2 = int(input("Masukkan angka kedua :"))
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi
k,l,m,n = operasi()

print(f"Hasil Tambah", k)
print(f"Hasil Kurang", l)
print(f"Hasil Kali", m)
print(f"Hasil Bagi", n)