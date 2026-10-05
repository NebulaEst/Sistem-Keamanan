print("===== PROGRAM CAESAR CIPHER =====")

nama = input("Masukkan Nama Mahasiswa: ")
nim = input("Masukkan NIM: ")
pesan = input("Masukkan Pesan Rahasia: ")
key = int(input("Masukkan Key: "))

ciphertext = ""

# Enkripsi
for huruf in pesan:
    if huruf.isalpha():
        if huruf.isupper():
            ciphertext += chr((ord(huruf) - 65 + key) % 26 + 65)
        else:
            ciphertext += chr((ord(huruf) - 97 + key) % 26 + 97)
    else:
        ciphertext += huruf

print()
print("===== HASIL ENKRIPSI =====")
print("Nama       :", nama)
print("NIM        :", nim)
print("Pesan Asli :", pesan)
print("Key        :", key)
print("Ciphertext :", ciphertext)

# Dekripsi
plaintext = ""

for huruf in ciphertext:
    if huruf.isalpha():
        if huruf.isupper():
            plaintext += chr((ord(huruf) - 65 - key) % 26 + 65)
        else:
            plaintext += chr((ord(huruf) - 97 - key) % 26 + 97)
    else:
        plaintext += huruf

print()
print("===== HASIL DEKRIPSI =====")
print("Plaintext  :", plaintext)