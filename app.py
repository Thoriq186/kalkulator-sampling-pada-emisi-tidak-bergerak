import streamlit as st
import math

st.set_page_config(page_title="Aplikasi Sampling Isokinetik", layout="centered")

# Navigasi halaman di bagian atas
menu = st.radio("📂 Pilih Halaman", ["Metode 1 Isokinetik", "About Us"], horizontal=True)

# Halaman: Metode 1 Isokinetik
if menu == "Metode 1 Isokinetik":
    st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
    st.header(":blue[Metode 1 - Isokinetik Sampling]")

    st.write("""
    Aplikasi ini membantu menghitung titik sampling pada cerobong untuk metode isokinetik berdasarkan jumlah titik lintas dan diameter cerobong.
    """)

    st.subheader("🧮 Input Parameter")
    diameter = st.number_input("Diameter Cerobong (cm)", min_value=1.0, step=0.1)
    jumlah_titik = st.number_input("Jumlah Titik Lintas", min_value=1, step=1)
    panjang_nipple = st.number_input("Panjang Nipple (cm)", min_value=0.0, step=0.1)
    upstream = st.number_input("Jarak Upstream (cm)", min_value=0.0, step=0.1)
    downstream = st.number_input("Jarak Downstream (cm)", min_value=0.0, step=0.1)

    st.markdown("---")

    if st.button("Hitung Titik Sampling"):
        if diameter and jumlah_titik:
            radius = diameter / 2
            st.subheader("📍 Titik Sampling yang Direkomendasikan")
            st.write(f"Diameter cerobong: **{diameter} cm**")
            st.write(f"Jumlah titik lintas: **{jumlah_titik} titik**")

            hasil = []
            for i in range(1, int(jumlah_titik) + 1):
                posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
                jarak_dari_tepi = round(radius - posisi, 2)
                hasil.append(jarak_dari_tepi)
                st.write(f"Titik {i}: {jarak_dari_tepi} cm dari tepi cerobong")

            st.success("Perhitungan selesai.")

            st.subheader("📋 Tabel Titik Sampling")
            st.table({f"Titik {i+1}": [f"{hasil[i]} cm"] for i in range(len(hasil))})
        else:
            st.error("Masukkan diameter dan jumlah titik yang valid.")

# Halaman: About Us
elif menu == "About Us":
    st.title("👨‍🔬 Tentang Aplikasi Ini")
    st.write("""
    Aplikasi ini dikembangkan untuk membantu teknisi atau mahasiswa dalam melakukan perhitungan titik sampling berdasarkan 
    **Metode 1 Isokinetik** yang digunakan dalam pengambilan sampel emisi dari sumber tidak bergerak seperti cerobong asap.

    **Fitur Aplikasi:**
    - Perhitungan otomatis berdasarkan jumlah titik lintas dan diameter cerobong.
    - Visualisasi sederhana hasil sampling.
    - Mudah digunakan dan berbasis web dengan Streamlit.

    **Pengembang:**
    - Nama: [Isikan Nama Anda]
    - Kontak: [Email atau media sosial]

    Aplikasi ini bersifat edukatif dan bebas digunakan.
    """)
    st.caption("📘 Dibuat dengan Streamlit - Open Source Project.")
