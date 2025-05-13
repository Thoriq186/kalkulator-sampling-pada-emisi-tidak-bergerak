import streamlit as st
import math

st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

# Title
st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
st.header(":blue[Metode 1 - Isokinetik Sampling]")

st.write("""
Aplikasi ini akan menghitung lokasi titik sampling cerobong berdasarkan diameter dan jarak terhadap gangguan aliran sesuai standar metode 1 isokinetik.
""")

#Navigasi menggunakan radio button
halaman = st.radio("Pilih Halaman", [ "Penjelasan & Informasi 💡", "Kalkulator Titik sampling 🧮"])

if halaman == "Penjelasan & Informasi 💡":
    st.title("Informasi Mengenai sampling Emisi Tidak Bergerak")

    st.markdown("""
    ## Apa itu Sampling Emisi Tidak Bergerak?
    Sampling emisi tidak bergerak adalah proses pengambilan cotoh gas buang dari sumber tetp, seperti cerobong industri untuk dianalisis kandungan plutannya. Ini penting untu mengevaluasi tigkat pencemaran udara dan kepatuhan terhadap regulasi lingkungan.

    ### Tujuan Sampling
    - Mengetahui konsentrasi polutan seperti SO₂, NOx, CO, NH₃, dan partikulat (TSP, PM10).
    - Menilai efisiensi alat pengendali polusi udara.
    - Memenuhi persyaratan peraturan pemerintah (SNI, Permen LH, USEPA).

    ### Metode Sampling Isokinetik
    - Sampling isokinetik dilakukan dengan menyamakan kecepatan aliran gas masuk probe dengan kecepatan gas buang di cerobong.
    - Penting untuk mencegah over-sampling atau under-sampling.
    - Menggunakan metode pembagian luas penampang cerobong (equal area) untuk menentukan titik pengambilan sampel.

    ### Standar dan Regulasi
    - SNI 7119.1:2017
    - USEPA Method 1–5
    - Permen LH No. 13 Tahun 2009
    """)
    
elif halaman == "Kalkulator Titik Sampling":
    st.title("Kalkulator Titik Sampling Cerobong Secara Isokinetik")
    
    st.markdown("""
    Penentuan titik sampling dilakukan berdasarkan metode equal area, membagi luas penampang cerobong menjadi beberapa bagian sama.
    Rumus dasar:
    \[ r_i = R \sqrt{\frac{i}{n}} \]
    \[ d_i = R - r_i \]

    Dimana:
    - \( R \): Jari-jari cerobong (cm)
    - \( i \): Titik ke-i
    - \( n \): Jumlah titik
    - \( d_i \): Jarak dari dinding
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
