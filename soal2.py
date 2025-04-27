def hitung_kata(teks, kata_dicari):
    
    teks = teks.lower()
    kata_dicari = kata_dicari.lower()
    teks = teks.replace('.', '').replace(',', '')
    daftar_kata = teks.split()
    jumlah = daftar_kata.count(kata_dicari)
    return jumlah

kalimat = input("Masukkan kalimat: ")
kata = input("Masukkan kata yang ingin dihitung: ")

jumlah = hitung_kata(kalimat, kata)
print(f"Kata '{kata}' muncul sebanyak {jumlah} kali.")
