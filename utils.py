
from database import load_data

def rekomendasi():
    data = load_data()
    if not data:
        print("Tidak ada produk.")
        return

    print("Rekomendasi Berdasarkan Harga Termurah:")
    for p in sorted(data, key=lambda x: x["harga"])[:3]:
        print(p)

    print("\nRekomendasi Berdasarkan Rating Tertinggi:")
    for p in sorted(data, key=lambda x: x["rating"], reverse=True)[:3]:
        print(p)

    print("\nRekomendasi Berdasarkan Stok Terendah:")
    for p in sorted(data, key=lambda x: x["stok"])[:3]:
        print(p)
