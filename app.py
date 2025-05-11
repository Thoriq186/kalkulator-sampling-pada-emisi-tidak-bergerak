import streamlit as st
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
st.header(":blue[Metode 1 - Isokinetik Sampling]")

st.write("""
Aplikasi ini menghitung dan memvisualisasikan titik sampling berdasarkan metode isokinetik (EPA Method 1).
""")

with st.sidebar:
    st.header("Input Parameter")
    diameter = st.number_input("Diameter Cerobong (cm)", min_value=1.0, step=0.1)
    jumlah_titik = st.number_input("Jumlah Titik Lintas", min_value=1, step=1)
    panjang_nipple = st.number_input("Panjang Nipple (cm)", min_value=0.0, step=0.1)
    upstream = st.number_input("Jarak Upstream (cm)", min_value=0.0, step=0.1)
    downstream = st.number_input("Jarak Downstream (cm)", min_value=0.0, step=0.1)

st.markdown("---")

if st.button("Hitung Titik Sampling"):
    if diameter and jumlah_titik:
        radius = diameter / 2
        hasil = []
        posisi_dari_tepi = []

        for i in range(1, int(jumlah_titik) + 1):
            posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
            jarak_tepi = round(radius - posisi, 2)
            hasil.append(jarak_tepi)
            posisi_dari_tepi.append(posisi)

        st.subheader("📍 Titik Sampling (dari tepi cerobong)")
        for idx, jarak in enumerate(hasil):
            st.write(f"Titik {idx + 1}: {jarak} cm")

        st.subheader("📊 Visualisasi Titik Sampling")

        # Plot lingkaran cerobong
        fig, ax = plt.subplots()
        cerobong = plt.Circle((0, 0), radius, fill=False, color='gray', linestyle='--', linewidth=2)
        ax.add_artist(cerobong)

        for i, r in enumerate(posisi_dari_tepi):
            ax.plot([0, r], [0, 0], marker='o', label=f'Titik {i+1}')
            ax.text(r, 0.5, f'{round(radius - r, 2)} cm', fontsize=9)

        ax.set_aspect('equal', 'box')
        ax.set_xlim(-radius * 1.1, radius * 1.1)
        ax.set_ylim(-radius * 0.5, radius * 1.5)
        ax.axis('off')
        ax.set_title("Penampang Cerobong & Titik Sampling", fontsize=12)

        st.pyplot(fig)

        st.success("Perhitungan dan visualisasi selesai.")
    else:
        st.error("Masukkan nilai diameter dan jumlah titik lintas yang valid.")

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit dan Matplotlib untuk simulasi edukatif metode isokinetik.")
