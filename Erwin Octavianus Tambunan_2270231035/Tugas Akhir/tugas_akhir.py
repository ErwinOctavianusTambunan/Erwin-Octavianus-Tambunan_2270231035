#TUGAS AKHIR PRAKTIKUM
nama_pemesan = input("Masukan Nama Pemesan :")
alamat = input("Masukan Alamat :")
notelp = input("Masukan No Telepon :")
import datetime
hari_ini = datetime.date.today()
print("""
    ==============================
            Suguhan Coffee
        List Menu Minuman Kopi 
    ==============================
    A. Latte     : Rp 25.000
    B. Espresso  : Rp 20.000
    C. Cappucino : Rp 26.000
    D. Machiatto : Rp 23.000
    ==============================
    """)
pesan = str(input("masukkan list abjad menu kopi ="))
jumlahpesan = int(input("masukkan jumlah pesanan ="))
if pesan == "a":
        listnama = "latte"
        harga = (25000*jumlahpesan)
        totalharga =int(harga)
elif pesan == "b":
        listnama = "Espresso"
        harga = (20000*jumlahpesan)
        totalharga = int(harga)
elif pesan == "c":
        listnama = "Cappucino"
        harga = int(26000*jumlahpesan)
        totalharga = int(harga)
elif pesan == "d":
        listnama = "Machiatto"
        harga = int(23000*jumlahpesan)
        totalharga = int(harga)
else:
        listnama = "-"
        harga = "-"
        totalharga = "-"
print("----------------------------------")
print("**********SUGUHAN COFFEE**********")
print("----------------------------------")
print("Nama Pemesan :", nama_pemesan)
print("Alamat :", alamat)
print("No Telepon :", notelp)
print("tanggal", hari_ini)
print("Menu :", listnama)
print("Jumlah Pesan :", jumlahpesan)
print("Harga :", harga)
print("--------------------------")
print("Jumlah Bayar :", totalharga)
print("**********Terima  Kasih**********")