# Buat dictionary untuk menyimpan data rating makanan
ratings = {
    'Makanan A': 4.5,
    'Makanan B': 3.8,
    'Makanan C': 4.0,
    'Makanan D': 4.2,
    'Makanan E': 3.9
}

# Mengurutkan makanan dari yang tertinggi ke terendah
sorted_ratings = {k: v for k, v in sorted(ratings.items(), key=lambda item: item[1], reverse=True)}

# Menampilkan makanan berdasarkan rating tertinggi ke terendah
print("Makanan yang diurutkan berdasarkan rating tertinggi:")
for makanan, rating in sorted_ratings.items():
    print(f"{makanan}: {rating}")

# Menghitung rata-rata rating
total_rating = sum(ratings.values())
jumlah_makanan = len(ratings)
rata_rata = total_rating / jumlah_makanan

print(f"Rata-rata rating makanan: {rata_rata:.2f}")
