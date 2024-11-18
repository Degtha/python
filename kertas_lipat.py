def kertas_lipat():
    sk = int(input("Masukkan Sisi Sama kaki : "))
    if not (0 < sk < 1000):
        print ("Tidak dapat melebihi kapasitas")
        return
    b = int(input("Masukkan bilangan bulat :"))
    if not (0 < b < 100000):
        print ("Tidak dapat melebihi kapasitas")
        return
    
    total = int(sk*(2**b)/2)
    return total 
print(f"Jadi jumlah totalnya : ", kertas_lipat())
    
    