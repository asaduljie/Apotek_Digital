import json
import os

DATA_FILE = "produk.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def tambah_produk():
    data = load_data()
    nama = input("Nama Produk: ")
    stok = int(input("Stok: "))
    harga = float(input("Harga: "))
    rating = float(input("Rating (1-5): "))
    kategori = input("Kategori Produk: ") # New input for category
    produk = {
        "nama": nama,
        "stok": stok,
        "harga": harga,
        "rating": rating,
        "jaminan": False,
        "kategori": kategori # Add category to product dictionary
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

def cari_kategori():
    data = load_data()
    kategori = input("Masukkan kategori yang dicari: ") 
    hasil = [p for p in data if "kategori" in p and kategori.lower() == p["kategori"].lower()] 
    if hasil:
        print("Hasil Pencarian berdasarkan Kategori:")
        for p in hasil:
            print(p)
    else:
        print("Tidak ada produk dalam kategori tersebut.")
