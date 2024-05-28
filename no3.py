kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]

filtered_kata = [word for word in kata if len(word) >= 5]

filtered_kata.sort()

print(filtered_kata)
