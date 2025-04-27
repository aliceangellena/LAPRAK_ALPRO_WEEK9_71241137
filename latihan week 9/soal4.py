import re

def cari_kata(kalimat):
    kata_kata = re.findall(r'\b\w+\b', kalimat)
    
    if not kata_kata:
        return None, None

    terpendek = min(kata_kata, key=len)
    terpanjang = max(kata_kata, key=len)
    
    return terpendek, terpanjang

kalimat_input = input("Masukkan sebuah kalimat: ")

kata_terpendek, kata_terpanjang = cari_kata(kalimat_input)

print(f"Kata terpendek: {kata_terpendek}")
print(f"Kata terpanjang: {kata_terpanjang}")