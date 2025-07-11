from models import (
    tambah_produk,
    update_stok,
    cari_produk,
    tampilkan_produk,
    jaminan_risiko,
    cari_kategori,
    hapus_produk  # Tambahkan ini
)

from utils import rekomendasi

def tampilkan_menu():
    while True:
        print("\n=== Sistem Informasi Apotek Digital ===")
        print("1. Tambah Produk")
        print("2. Update Stok")
        print("3. Cari Produk")
        print("4. Tampilkan Semua Produk")
        print("5. Tambah Jaminan Risiko")
        print("6. Tampilkan Rekomendasi")
        print("7. Cari Produk Berdasarkan Kategori")
        print("8. Hapus Produk")  # Tambahkan ini
        print("0. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tambah_produk()
        elif pilihan == "2":
            update_stok()
        elif pilihan == "3":
            cari_produk()
        elif pilihan == "4":
            tampilkan_produk()
        elif pilihan == "5":
            jaminan_risiko()
        elif pilihan == "6":
            rekomendasi()
        elif pilihan == "7":
            cari_kategori()
        elif pilihan == "8":
            hapus_produk()  
        elif pilihan == "0":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid.")
