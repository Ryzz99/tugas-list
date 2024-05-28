# List awal
numbers = [105, 20, 8, 150, 30, 5, 200]

# Menghapus nilai yang kurang dari 10 dan lebih dari 100
filtered_numbers = [num for num in numbers if 10 <= num <= 100]

# Mengurutkan nilai yang tersisa dari terkecil ke terbesar
filtered_numbers.sort()

# Menampilkan output
print(filtered_numbers)
