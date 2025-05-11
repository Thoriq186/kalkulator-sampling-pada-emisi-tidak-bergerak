import streamlit as st
import math

st.set_page_config(page_title="Simulasi Edukasi Limbah Industri", layout="centered")

# Session state untuk navigasi
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "home"

def go_to_metode_1():
    st.session_state["halaman"] = "metode_1"

# --- Tampilan Home ---
if st.session_state["halaman"] == "home":
    st.markdown("<h1 style='text-align: center;'>♻️ Manajemen & Edukasi Limbah Industri ♻️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Belajar dan simulasi proses pengolahan limbah industri secara interaktif dan edukatif.</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://img.icons8.com/external-flat-juicy-fish/512/external-process-engineering-flat-flat-juicy-fish.png", width=100)
        st.button("🧪 Edukasi Proses", on_click=go_to_metode_1)
        st.caption("Simulasi proses pengolahan limbah dari awal hingga akhir.")

    with col2:
        st.image("https://img.icons8.com/color/512/laboratory.png", width=100)
        st.caption("Hitung nilai COD, BOD, TSS, dan pH dari data sampel.")

    with col3:
        st.image("https://img.icons8.com/office/512/water-pollution.png", width=100)
        st.caption("Simulasi interaktif pengolahan limbah berbagai jenis.")

# --- Halaman Metode 1 ---
elif st.session_state["halaman"] == "metode_1":
    st.title("📏 Kalkulator Titik Sampling - Metode 1 Isokinetik 💨")
    st.write("""
    Aplikasi ini membantu menghitung titik sampling pada cerobong untuk metode isokinetik berdasarkan jumlah titik lintas dan diameter cerobong.
    """)

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

    if st.button("🔙 Kembali ke Beranda"):
        st.session_state["halaman"] = "home"
