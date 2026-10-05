def rot13(text):
    hasil = ""
    for char in text:
        if char.isalpha():
            dasar = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - dasar + 13) % 26 + dasar)
        else:
            hasil += char
    return hasil

pesan = input("Masukkan pesan: ")

ciphertext = rot13(pesan)
plaintext = rot13(ciphertext)

print("\nPesan awal: ", pesan)
print("ROT13       : ", ciphertext)
print("Kembali     : ", plaintext)