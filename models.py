
from database import load_data, save_data

def tambah_produk():
    data = load_data()
    nama = input("Nama Produk: ")
    stok = int(input("Stok: "))
    harga = float(input("Harga: "))
    rating = float(input("Rating (1-5): "))
    produk = {
        "nama": nama,
        "stok": stok,
        "harga": harga,
        "rating": rating,
        "jaminan": False
    }
    data.append(produk)
    save_data(data)
    print("Produk berhasil ditambahkan.")

def update_stok():
    data = load_data()
    nama = input("Masukkan nama produk yang akan diupdate: ")
    for produk in data:
        if produk["nama"].lower() == nama.lower():
            new_stok = int(input("Masukkan stok baru: "))
            produk["stok"] = new_stok
            save_data(data)
            print("Stok berhasil diperbarui.")
            return
    print("Produk tidak ditemukan.")

def cari_produk():
    data = load_data()
    keyword = input("Masukkan kata kunci: ")
    hasil = [p for p in data if keyword.lower() in p["nama"].lower()]
    if hasil:
        print("Hasil Pencarian:")
        for p in hasil:
            print(p)
    else:
        print("Produk tidak ditemukan.")

def tampilkan_produk():
    data = load_data()
    if data:
        print("Daftar Produk:")
        for p in data:
            print(p)
    else:
        print("Tidak ada produk.")

def jaminan_risiko():
    data = load_data()
    nama = input("Masukkan nama produk untuk ditambahkan jaminan risiko: ")
    for produk in data:
        if produk["nama"].lower() == nama.lower():
            produk["jaminan"] = True
            save_data(data)
            print("Jaminan risiko ditambahkan.")
            return
    print("Produk tidak ditemukan.")
