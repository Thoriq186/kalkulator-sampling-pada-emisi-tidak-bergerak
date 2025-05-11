import streamlit as st
import math

# Konfigurasi awal halaman
st.set_page_config(page_title="Edukasi Limbah Industri", layout="centered")

# Inisialisasi session state
if "halaman" not in st.session_state:
    st.session_state["halaman"] = "beranda"

def buka_metode_1():
    st.session_state["halaman"] = "metode_1"

def buka_about():
    st.session_state["halaman"] = "about"

# ================= HALAMAN BERANDA =================
if st.session_state["halaman"] == "beranda":
    st.markdown("<h1 style='text-align: center;'>📚 Edukasi Limbah Industri</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Simulasi interaktif & edukatif untuk pengolahan limbah industri</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://img.icons8.com/external-flat-juicy-fish/512/external-process-engineering-flat-flat-juicy-fish.png", use_column_width=True)
        if st.button("🧪 Metode 1 Isokinetik"):
            buka_metode_1()

    with col2:
        st.image("https://img.icons8.com/color/512/about.png", use_column_width=True)
        if st.button("ℹ️ About Us"):
            buka_about()

# ================= HALAMAN METODE 1 =================
elif st.session_state["halaman"] == "metode_1":
    st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
    st.header(":blue[Metode 1 - Isokinetik Sampling]")

    st.write("""
    Aplikasi ini membantu menghitung titik sampling pada cerobong untuk metode isokinetik berdasarkan jumlah titik lintas dan diameter cerobong.
    """)

    diameter = st.number_input("Diameter Cerobong (m)", min_value=1.0, step=0.1)
    jumlah_titik = st.number_input("Jumlah Titik Lintas", min_value=1, step=1)
    panjang_nipple = st.number_input("Panjang Nipple (m)", min_value=0.0, step=0.1)
    upstream = st.number_input("Jarak Upstream (m)", min_value=0.0, step=0.1)
    downstream = st.number_input("Jarak Downstream (m)", min_value=0.0, step=0.1)

    st.markdown("---")

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

            # Tampilkan tabel hasil
            st.subheader("📋 Tabel Titik Sampling")
            st.table({f"Titik {i+1}": [f"{hasil[i]} m"] for i in range(len(hasil))})
        else:
            st.error("Masukkan diameter dan jumlah titik yang valid.")

    if st.button("🔙 Kembali ke Beranda"):
        st.session_state["halaman"] = "beranda"

# ================= HALAMAN ABOUT =================
elif st.session_state["halaman"] == "about":
    st.title("ℹ️ Tentang Aplikasi")
    st.write("""
    Aplikasi ini dikembangkan untuk edukasi dan simulasi dalam bidang pengolahan limbah industri.

    **Fitur yang tersedia:**
    - Kalkulator Metode 1 Isokinetik
    - Uji Laboratorium (dalam pengembangan)
    - Simulasi interaktif (dalam pengembangan)

    Dibuat menggunakan Python & Streamlit oleh tim pengembang edukasi lingkungan.
    """)
    st.markdown("---")
    if st.button("🔙 Kembali ke Beranda"):
        st.session_state["halaman"] = "beranda"
