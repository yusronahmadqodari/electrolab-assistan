# ==========================================
#       KALKULATOR RESISTOR 4 & 5 GELANG
# ==========================================

# Dictionary nilai angka warna
warna = {
    "hitam": 0,
    "cokelat": 1,
    "merah": 2,
    "oranye": 3,
    "kuning": 4,
    "hijau": 5,
    "biru": 6,
    "ungu": 7,
    "abu-abu": 8,
    "putih": 9
}

# Dictionary nilai multiplier
multiplier = {
    "hitam": 1,
    "cokelat": 10,
    "merah": 100,
    "oranye": 1000,
    "kuning": 10000,
    "hijau": 100000,
    "biru": 1000000,
    "ungu": 10000000
}

# Dictionary nilai toleransi
toleransi = {
    "cokelat": 1,
    "merah": 2,
    "hijau": 0.5,
    "biru": 0.25,
    "ungu": 0.1,
    "emas": 5,
    "perak": 10
}


# ==========================================
# FUNCTION UNTUK MENGHITUNG RESISTOR 4 GELANG
# ==========================================

def resistor_4_gelang(gelang1, gelang2, gelang3, gelang4):

    angka1 = warna[gelang1]
    angka2 = warna[gelang2]

    # Menggabungkan dua angka pertama
    angka = angka1 * 10 + angka2

    # Menghitung nilai resistor
    nilai = angka * multiplier[gelang3]

    # Mengambil nilai toleransi
    persen = toleransi[gelang4]

    # Menghitung rentang
    minimum = nilai - (nilai * persen / 100)
    maksimum = nilai + (nilai * persen / 100)

    return nilai, persen, minimum, maksimum


# ==========================================
# FUNCTION UNTUK MENGHITUNG RESISTOR 5 GELANG
# ==========================================

def resistor_5_gelang(gelang1, gelang2, gelang3, gelang4, gelang5):

    angka1 = warna[gelang1]
    angka2 = warna[gelang2]
    angka3 = warna[gelang3]

    # Menggabungkan tiga angka pertama
    angka = angka1 * 100 + angka2 * 10 + angka3

    # Menghitung nilai resistor
    nilai = angka * multiplier[gelang4]

    # Mengambil nilai toleransi
    persen = toleransi[gelang5]

    # Menghitung rentang
    minimum = nilai - (nilai * persen / 100)
    maksimum = nilai + (nilai * persen / 100)

    return nilai, persen, minimum, maksimum


# ==========================================
# PROGRAM UTAMA
# ==========================================

print("====================================")
print("       KALKULATOR RESISTOR")
print("====================================")

print("\nPilih jenis resistor:")
print("1. Resistor 4 Gelang")
print("2. Resistor 5 Gelang")

jenis = input("Masukkan pilihan (1/2): ")


# ==========================================
# RESISTOR 4 GELANG
# ==========================================

if jenis == "1":

    print("\n--- RESISTOR 4 GELANG ---")

    print("\nWarna angka:")
    print("Hitam, Cokelat, Merah, Oranye, Kuning")
    print("Hijau, Biru, Ungu, Abu-abu, Putih")

    print("\nWarna toleransi:")
    print("Cokelat, Merah, Hijau, Biru, Ungu, Emas, Perak")

    gelang1 = input("\nGelang 1: ").lower()
    gelang2 = input("Gelang 2: ").lower()
    gelang3 = input("Gelang 3 (Multiplier): ").lower()
    gelang4 = input("Gelang 4 (Toleransi): ").lower()

    # Mengecek input
    if (gelang1 in warna and
        gelang2 in warna and
        gelang3 in multiplier and
        gelang4 in toleransi):

        nilai, persen, minimum, maksimum = resistor_4_gelang(
            gelang1, gelang2, gelang3, gelang4
        )

        print("\n========== HASIL ==========")
        print("Jenis       : 4 Gelang")
        print("Kode Warna  :", gelang1, "-", gelang2, "-", gelang3, "-", gelang4)
        print("Resistansi  :", nilai, "Ohm")
        print("Toleransi   : ±", persen, "%")
        print("Minimum     :", minimum, "Ohm")
        print("Maksimum    :", maksimum, "Ohm")
        print("============================")

    else:
        print("\nWarna yang dimasukkan tidak valid!")


# ==========================================
# RESISTOR 5 GELANG
# ==========================================

elif jenis == "2":

    print("\n--- RESISTOR 5 GELANG ---")

    print("\nWarna angka:")
    print("Hitam, Cokelat, Merah, Oranye, Kuning")
    print("Hijau, Biru, Ungu, Abu-abu, Putih")

    print("\nWarna toleransi:")
    print("Cokelat, Merah, Hijau, Biru, Ungu, Emas, Perak")

    gelang1 = input("\nGelang 1: ").lower()
    gelang2 = input("Gelang 2: ").lower()
    gelang3 = input("Gelang 3: ").lower()
    gelang4 = input("Gelang 4 (Multiplier): ").lower()
    gelang5 = input("Gelang 5 (Toleransi): ").lower()

    # Mengecek input
    if (gelang1 in warna and
        gelang2 in warna and
        gelang3 in warna and
        gelang4 in multiplier and
        gelang5 in toleransi):

        nilai, persen, minimum, maksimum = resistor_5_gelang(
            gelang1, gelang2, gelang3, gelang4, gelang5
        )

        print("\n========== HASIL ==========")
        print("Jenis       : 5 Gelang")
        print("Kode Warna  :", gelang1, "-", gelang2, "-", gelang3, "-", gelang4, "-", gelang5)
        print("Resistansi  :", nilai, "Ohm")
        print("Toleransi   : ±", persen, "%")
        print("Minimum     :", minimum, "Ohm")
        print("Maksimum    :", maksimum, "Ohm")
        print("============================")

    else:
        print("\nWarna yang dimasukkan tidak valid!")


# ==========================================
# JIKA PILIHAN SALAH
# ==========================================

else:
    print("\nPilihan tidak valid!")
    print("Silakan pilih 1 atau 2.")