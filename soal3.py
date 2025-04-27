import re

def bersihkan_spasi(teks):
    return re.sub(r'\s+', ' ', teks).strip()

input_anda = input("Masukkan teks yang ingin dibersihkan: ")

hasil_bersih = bersihkan_spasi(input_anda)

print("\nHasil setelah dibersihkan:")
print(f"\"{hasil_bersih}\"")