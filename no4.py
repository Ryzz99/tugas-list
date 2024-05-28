# List buah-buahan pertama
list1 = ["apel", "jeruk", "mangga"]

# List buah-buahan kedua
list2 = ["apel", "anggur", "nanas"]

# Menggabungkan kedua list
combined_list = list1 + list2

# Menghapus buah yang memiliki nama yang sama
unique_fruits = []
for fruit in combined_list:
    if fruit not in unique_fruits:
        unique_fruits.append(fruit)

# Mengurutkan sisa buah-buahan secara alfabetis
unique_fruits.sort()

# Menampilkan output
print(unique_fruits)
