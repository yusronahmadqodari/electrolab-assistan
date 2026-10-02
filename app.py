import streamlit as st

st.set_page_config(
    page_title="ElectroLab Assistant",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ElectroLab Assistant")
st.write("Asisten Praktikum Elektronika")

st.divider()

st.subheader("Pilih Fitur")

# ==============================
# MENU UTAMA
# ==============================

st.subheader("🔧 Pilih Fitur")

fitur = st.selectbox(
    "Pilih fitur yang ingin digunakan:",
    [
        "⚡ Hukum Ohm",
        "🔋 Kalkulator Daya",
        "🔗 Resistor Seri & Paralel",
        "📐 Konversi Satuan",
        "📈 Waveform Checker",
        "📋 Riwayat Perhitungan"
    ]
)

# ==============================
# 1. HUKUM OHM
# ==============================

if fitur == "⚡ Hukum Ohm":

    st.header("⚡ Kalkulator Hukum Ohm")

    pilihan = st.selectbox(
        "Apa yang ingin dihitung?",
        ["Tegangan (V)", "Arus (I)", "Resistansi (R)"]
    )

    if pilihan == "Tegangan (V)":

        I = st.number_input("Arus (A)", min_value=0.0)
        R = st.number_input("Resistansi (Ω)", min_value=0.0)

        if st.button("Hitung Tegangan"):
            V = I * R
            st.success(f"Tegangan = {V:.2f} V")

    elif pilihan == "Arus (I)":

        V = st.number_input("Tegangan (V)", min_value=0.0)
        R = st.number_input("Resistansi (Ω)", min_value=0.0)

        if st.button("Hitung Arus"):
            if R != 0:
                I = V / R
                st.success(f"Arus = {I:.4f} A")
            else:
                st.error("Resistansi tidak boleh 0 Ω.")

    else:

        V = st.number_input("Tegangan (V)", min_value=0.0)
        I = st.number_input("Arus (A)", min_value=0.0)

        if st.button("Hitung Resistansi"):
            if I != 0:
                R = V / I
                st.success(f"Resistansi = {R:.2f} Ω")
            else:
                st.error("Arus tidak boleh 0 A.")


# ==============================
# 2. KALKULATOR DAYA
# ==============================

elif fitur == "🔋 Kalkulator Daya":

    st.header("🔋 Kalkulator Daya")

    V = st.number_input("Tegangan (V)", min_value=0.0)
    I = st.number_input("Arus (A)", min_value=0.0)

    if st.button("Hitung Daya"):
        P = V * I
        st.success(f"Daya = {P:.2f} Watt")


# ==============================
# 3. RESISTOR SERI & PARALEL
# ==============================

elif fitur == "🔗 Resistor Seri & Paralel":

    st.header("🔗 Resistor Seri & Paralel")

    jumlah = st.number_input(
        "Jumlah resistor",
        min_value=2,
        max_value=10,
        value=2,
        step=1
    )

    resistor = []

    for i in range(int(jumlah)):
        R = st.number_input(
            f"R{i+1} (Ω)",
            min_value=0.0,
            key=f"resistor_{i}"
        )
        resistor.append(R)

    mode = st.radio(
        "Jenis rangkaian:",
        ["Seri", "Paralel"]
    )

    if st.button("Hitung Resistansi Total"):

        if mode == "Seri":

            hasil = sum(resistor)
            st.success(f"Resistansi total seri = {hasil:.2f} Ω")

        else:

            if 0 in resistor:
                st.error("Resistansi tidak boleh 0 Ω.")
            else:
                hasil = 1 / sum(1 / R for R in resistor)
                st.success(
                    f"Resistansi total paralel = {hasil:.2f} Ω"
                )


# ==============================
# 4. KONVERSI SATUAN
# ==============================

elif fitur == "📐 Konversi Satuan":

    st.header("📐 Konversi Satuan")

    jenis = st.selectbox(
        "Pilih konversi:",
        [
            "Volt → Milivolt",
            "Milivolt → Volt",
            "Ohm → Kiloohm",
            "Kiloohm → Ohm",
            "Ampere → Miliampere",
            "Miliampere → Ampere"
        ]
    )

    nilai = st.number_input("Masukkan nilai:", min_value=0.0)

    if st.button("Konversi"):

        if jenis == "Volt → Milivolt":
            hasil = nilai * 1000
            satuan = "mV"

        elif jenis == "Milivolt → Volt":
            hasil = nilai / 1000
            satuan = "V"

        elif jenis == "Ohm → Kiloohm":
            hasil = nilai / 1000
            satuan = "kΩ"

        elif jenis == "Kiloohm → Ohm":
            hasil = nilai * 1000
            satuan = "Ω"

        elif jenis == "Ampere → Miliampere":
            hasil = nilai * 1000
            satuan = "mA"

        else:
            hasil = nilai / 1000
            satuan = "A"

        st.success(f"Hasil = {hasil:.4f} {satuan}")


# ==============================
# 5. WAVEFORM CHECKER
# ==============================

elif fitur == "📈 Waveform Checker":

    st.header("📈 Waveform Checker")

    import math

    amplitudo = st.number_input(
        "Amplitudo",
        min_value=0.0,
        value=1.0
    )

    frekuensi = st.number_input(
        "Frekuensi (Hz)",
        min_value=0.1,
        value=1.0
    )

    if st.button("Tampilkan Grafik"):

        waktu = [i / 100 for i in range(501)]

        gelombang = [
            amplitudo * math.sin(
                2 * math.pi * frekuensi * t
            )
            for t in waktu
        ]

        data = {
            "Waktu (s)": waktu,
            "Amplitudo": gelombang
        }

        st.line_chart(
            data,
            x="Waktu (s)",
            y="Amplitudo"
        )

        st.success("Grafik gelombang berhasil dibuat!")


# ==============================
# 6. RIWAYAT PERHITUNGAN
# ==============================

elif fitur == "📋 Riwayat Perhitungan":

    st.header("📋 Riwayat Perhitungan")

    st.info(
        "Fitur riwayat akan digunakan untuk menyimpan "
        "hasil perhitungan yang dilakukan selama aplikasi berjalan."
    )

    st.write("Belum ada riwayat perhitungan.")