import re
from datetime import datetime

def proses_tanggal(teks):
    pola = r'\b\d{4}-\d{2}-\d{2}\b'
    tanggal_temu = re.findall(pola, teks)
    sekarang = datetime.now()
    
    hasil = []
    for tgl_str in tanggal_temu:
        tgl = datetime.strptime(tgl_str, '%Y-%m-%d')

        tgl_baru = tgl.strftime('%d-%m-%Y')

        selisih = (sekarang - tgl).days

        hasil.append(f"{tgl_str} 00:00:00 selisih {selisih} hari")
    
    return hasil

teks_contoh = """Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
Hajar Dewantara (1889-05-02)."""

hasil = proses_tanggal(teks_contoh)
for item in hasil:
    print(item)