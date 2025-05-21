import streamlit as st
import math

st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

# Title
st.title(" 📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
st.header(":blue[Metode 1 - Isokinetik Sampling]")

st.write("""
Aplikasi ini akan menghitung lokasi titik sampling cerobong berdasarkan diameter dan jarak terhadap gangguan aliran sesuai standar metode 1 isokinetik.
""")

# Sidebar Input
with st.sidebar:
    st.header("Navigasi Halaman")
    halaman = st.radio("Pilih Halaman", ["Penjelasan & Informasi 💡", "Kalkulator Titik Sampling 🧮"])

    if halaman == "Kalkulator Titik Sampling 🧮":
        st.header("Input Parameter")
        diameter = st.number_input("Diameter Cerobong (m)", min_value=0.1, step=0.01)
        panjang_nipple = st.number_input("Panjang Nipple (m)", min_value=0.0, step=0.1)
        upstream = st.number_input("Jarak Upstream dari Gangguan (m)", min_value=0.0, step=0.1)
        downstream = st.number_input("Jarak Downstream dari Gangguan (m)", min_value=0.0, step=0.1)
        hitung = st.button("🔍 Hitung Titik Sampling")
    else:
        diameter = panjang_nipple = upstream = downstream = hitung = None

# Fungsi Penentu Titik
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

# Konten Utama: Kalkulator
if halaman == "Kalkulator Titik Sampling 🧮":
    if hitung and diameter:
        jumlah_titik = tentukan_jumlah_titik(diameter, upstream, downstream)
        radius = diameter / 2
        hasil = []
        for i in range(1, jumlah_titik + 1):
            posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
            jarak_dari_tepi = round(radius - posisi, 3)
            hasil.append((f"Titik {i}", f"{jarak_dari_tepi} m"))

        # 🔽 Hasil DITAMPILKAN di ATAS rumus
        st.subheader("📍 Hasil Perhitungan Titik Sampling")
        st.write(f"Diameter cerobong: **{diameter} m**")
        st.write(f"Jumlah titik lintas: **{jumlah_titik} titik**")
        st.table(dict(hasil))
        st.success("Perhitungan titik sampling selesai.")

    # Penjelasan metode (di bawah hasil)
    st.markdown(r"""
    ### 📐 Rumus Dasar

    Untuk metode equal area:

    $$
    r_i = R \cdot \sqrt{\frac{i}{n}}
    $$

    $$
    d_i = R - r_i
    $$

    **Dimana:**
    - \( R \): Jari-jari cerobong (m)  
    - \( i \): Titik sampling ke-i  
    - \( n \): Jumlah titik sampling  
    - \( d_i \): Jarak dari dinding ke titik sampling ke-i
    """)

# Konten Informasi
elif halaman == "Penjelasan & Informasi 💡":
    st.title("Informasi Mengenai Sampling Emisi Tidak Bergerak")
    st.markdown("""
    ## Apa itu Sampling Emisi Tidak Bergerak?
    Sampling emisi tidak bergerak adalah proses pengambilan contoh gas buang dari sumber tetap, seperti cerobong industri, untuk dianalisis kandungan polutannya. Ini penting untuk mengevaluasi tingkat pencemaran udara dan kepatuhan terhadap regulasi lingkungan.

    ### Tujuan Sampling
    - Mengetahui konsentrasi polutan seperti SO₂, NOx, CO, NH₃, dan partikulat (TSP, PM10).
    - Menilai efisiensi alat pengendali polusi udara.
    - Memenuhi persyaratan peraturan pemerintah (SNI, Permen LH, USEPA).

    ### Metode Sampling Isokinetik
    - Sampling isokinetik dilakukan dengan menyamakan kecepatan aliran gas masuk probe dengan kecepatan gas buang di cerobong.
    - Penting untuk mencegah over-sampling atau under-sampling.
    - Menggunakan metode pembagian luas penampang cerobong (equal area) untuk menentukan titik pengambilan sampel.

    ### Standar dan Regulasi
    - SNI 7117.13.2009
    - USEPA Method 1–5
    - Permen LH No. 13 Tahun 2009
    """)

st.markdown("---")
st.caption("📘 Dibuat dengan Streamlit berdasarkan metode sampling isokinetik sesuai standar EPA.")
