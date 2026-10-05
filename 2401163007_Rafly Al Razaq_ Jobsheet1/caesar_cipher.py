def caesar_encrypt(text, shift):
    hasil = ""
    for char in text:
        if char.isalpha():
            dasar = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - dasar + shift) % 26 + dasar)
        else:
            hasil += char
    return hasil

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

pesan = input("Masukkan pesan: ")
shift = int(input("Masukkan jumlah pergeseran: "))

ciphertext = caesar_encrypt(pesan, shift)
plaintext = caesar_decrypt(ciphertext, shift)

print("Pesan asli:", pesan)
print("Ciphertext:", ciphertext)
print("Plaintext:", plaintext)