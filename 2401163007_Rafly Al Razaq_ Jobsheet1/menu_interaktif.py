print("==============================")
print("   PROGRAM KEAMANAN INFORMASI")
print("==============================")
print("1. Caesar Cipher")
print("2. ROT13")
print("3. Keluar")

pilih = input("Pilih menu: ")

if pilih == "1":
    plaintext = input("Masukkan plaintext: ")
    shift = int(input("Masukkan shift: "))

    ciphertext = ""

    for huruf in plaintext:
        if huruf.isalpha():
            if huruf.isupper():
                ciphertext += chr((ord(huruf) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(huruf) - 97 + shift) % 26 + 97)
        else:
            ciphertext += huruf

    print("Ciphertext:", ciphertext)

    hasil = ""

    for huruf in ciphertext:
        if huruf.isalpha():
            if huruf.isupper():
                hasil += chr((ord(huruf) - 65 - shift) % 26 + 65)
            else:
                hasil += chr((ord(huruf) - 97 - shift) % 26 + 97)
        else:
            hasil += huruf

    print("Plaintext kembali:", hasil)

elif pilih == "2":
    plaintext = input("Masukkan plaintext: ")

    ciphertext = ""

    for huruf in plaintext:
        if huruf.isalpha():
            if huruf.isupper():
                ciphertext += chr((ord(huruf) - 65 + 13) % 26 + 65)
            else:
                ciphertext += chr((ord(huruf) - 97 + 13) % 26 + 97)
        else:
            ciphertext += huruf

    print("Ciphertext:", ciphertext)

    hasil = ""

    for huruf in ciphertext:
        if huruf.isalpha():
            if huruf.isupper():
                hasil += chr((ord(huruf) - 65 + 13) % 26 + 65)
            else:
                hasil += chr((ord(huruf) - 97 + 13) % 26 + 97)
        else:
            hasil += huruf

    print("Plaintext kembali:", hasil)

elif pilih == "3":
    print("Program selesai.")

else:
    print("Menu tidak tersedia.")