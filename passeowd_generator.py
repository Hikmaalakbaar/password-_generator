import random
import string

def generate_password(length):
    # Definisikan karakter yang akan digunakan dalam password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Menggunakan random.choices untuk memilih karakter secara acak
    password = ''.join(random.choices(characters, k=length))
    return password

# Minta input panjang password dari pengguna
length = int(input("Masukkan panjang password yang diinginkan: "))

# Hasilkan password dan tampilkan
password = generate_password(length)
print("Password yang dihasilkan:", password)
