import re

def bersihkan_kata(kata):
    return re.sub(r'[^a-zA-Z]', '', kata).lower()

def is_anagram(kata1, kata2):
    kata1_bersih = bersihkan_kata(kata1)
    kata2_bersih = bersihkan_kata(kata2)

    if len(kata1_bersih) != len(kata2_bersih):
        return False

    return sorted(kata1_bersih) == sorted(kata2_bersih)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if is_anagram(kata1, kata2):
    print(f"'{kata1}' dan '{kata2}' adalah anagram")
else:
    print(f"'{kata1}' dan '{kata2}' bukan anagram")