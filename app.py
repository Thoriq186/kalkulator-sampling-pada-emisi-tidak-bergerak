import streamlit as st
import math

st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

# Title
st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
st.header(":blue[Metode 1 - Isokinetik Sampling]")

st.write("""
Aplikasi ini akan menghitung lokasi titik sampling cerobong berdasarkan diameter dan jarak terhadap gangguan aliran sesuai standar metode 1 isokinetik.
""")

# Sidebar for input
with st.sidebar:
    st.header("Input Parameter")
    diameter = st.number_input("Diameter Cerobong (m)", min_value=0.1, step=0.01)
    panjang_nipple = st.number_input("Panjang Nipple (m)", min_value=0.0, step=0.1)
    upstream = st.number_input("Jarak Upstream dari Gangguan (m)", min_value=0.0, step=0.1)
    downstream = st.number_input("Jarak Downstream dari Gangguan (m)", min_value=0.0, step=0.1)

# Divider
st.markdown("---")

# Fungsi menentukan jumlah titik lintas
def tentukan_jumlah_titik(diameter, upstream, downstream):
    if diameter >= 0.61:
        if upstream >= 8 * diameter and downstream >= 2 * diameter:
            return 12
        elif upstream >= 4 * diameter and downstream >= 1 * diameter:
            return 10
        else:
            return 8
    elif 0.3 <= diameter < 0.61:
        return 8
    else:
        return 6

# Tombol Hitung
if st.button("Hitung Titik Sampling"):
    if diameter > 0:
        jumlah_titik = tentukan_jumlah_titik(diameter, upstream, downstream)
        radius = diameter / 2
        st.subheader("📍 Hasil Perhitungan")
        st.write(f"Diameter cerobong: **{diameter} m**")
        st.write(f"Jumlah titik lintas (otomatis): **{jumlah_titik} titik**")

        hasil = []
        for i in range(1, jumlah_titik + 1):
            posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
            jarak_dari_tepi = round(radius - posisi, 3)
            hasil.append(jarak_dari_tepi)
            st.write(f"Titik {i}: {jarak_dari_tepi} m dari tepi cerobong")

        # Tabel hasil
        st.subheader("📋 Tabel Titik Sampling")
        st.table({f"Titik {i+1}": [f"{hasil[i]} m"] for i in range(len(hasil))})

        st.success("Perhitungan titik sampling selesai.")
    else:
        st.error("Masukkan diameter cerobong yang valid.")

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit berdasarkan metode sampling isokinetik sesuai standar EPA.")
