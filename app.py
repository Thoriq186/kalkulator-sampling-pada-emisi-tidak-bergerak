import streamlit as st
import math

st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

# Title
st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
st.header(":blue[Metode 1 - Isokinetik Sampling]")

# Home
if menu=='Home':
    

# Description
st.write("""
Aplikasi ini membantu menghitung titik sampling pada cerobong untuk metode isokinetik berdasarkan jumlah titik lintas dan diameter cerobong.
""")

# Sidebar for input
with st.sidebar:
    st.header("Input Parameter")
    diameter = st.number_input("Diameter Cerobong (m)", min_value=1.0, step=0.1)
    jumlah_titik = st.number_input("Jumlah Titik Lintas", min_value=1, step=1)
    panjang_nipple = st.number_input("Panjang Nipple (m)", min_value=0.0, step=0.1)
    upstream = st.number_input("Jarak Upstream (m)", min_value=0.0, step=0.1)
    downstream = st.number_input("Jarak Downstream (m)", min_value=0.0, step=0.1)

# Divider
st.markdown("---")

# Tombol untuk menghitung
if st.button("Hitung Titik Sampling"):
    if diameter and jumlah_titik:
        radius = diameter / 2
        st.subheader("📍 Titik Sampling yang Direkomendasikan")
        st.write(f"Diameter cerobong: **{diameter} m**")
        st.write(f"Jumlah titik lintas: **{jumlah_titik} titik**")

        hasil = []
        for i in range(1, int(jumlah_titik) + 1):
            posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
            jarak_dari_tepi = round(radius - posisi, 2)
            hasil.append(jarak_dari_tepi)
            st.write(f"Titik {i}: {jarak_dari_tepi} m dari tepi cerobong")

        st.success("Perhitungan selesai.")

        # Optional: Tampilkan tabel
        st.subheader("📋 Tabel Titik Sampling")
        st.table({f"Titik {i+1}": [f"{hasil[i]} m"] for i in range(len(hasil))})
    else:
        st.error("Masukkan diameter dan jumlah titik yang valid.")

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit untuk simulasi edukatif metode sampling isokinetik.")
