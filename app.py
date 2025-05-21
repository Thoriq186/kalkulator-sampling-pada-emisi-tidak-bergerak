import streamlit as st
import math
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Metode 1 Isokinetik Pada Emisi Tidak Bergerak", layout="centered")

# Judul Aplikasi
st.title("📏 Kalkulator Titik Sampling Pada Emisi Tidak Bergerak 💨")
st.header(":blue[Metode 1 - Isokinetik Sampling]")

st.write("""
Aplikasi ini akan menghitung lokasi titik sampling cerobong berdasarkan diameter dan jarak terhadap gangguan aliran sesuai standar metode 1 isokinetik.
""")

# Sidebar Navigasi
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

# Fungsi untuk menentukan jumlah titik lintas
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

# Halaman Kalkulator
if halaman == "Kalkulator Titik Sampling 🧮":
    if hitung and diameter:
        jumlah_titik = tentukan_jumlah_titik(diameter, upstream, downstream)
        radius = diameter / 2

        data_tabel = []
        for i in range(1, jumlah_titik + 1):
            posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
            jarak_dari_tepi = round(radius - posisi, 4)
            jarak_dari_pusat = round(posisi, 4)
            data_tabel.append({
                "Titik ke-": i,
                "Jarak dari tepi (m)": jarak_dari_tepi,
                "Jarak dari pusat (m)": jarak_dari_pusat
            })

        df_titik = pd.DataFrame(data_tabel)

        # Menampilkan hasil
        st.subheader("📍 Hasil Perhitungan Titik Sampling")
        st.write(f"Diameter cerobong: **{diameter} m**")
        st.write(f"Jumlah titik lintas (otomatis): **{jumlah_titik} titik**")

        st.subheader("📋 Tabel Titik Sampling")
        st.dataframe(df_titik, use_container_width=True)

        # Opsi unduh CSV
        csv = df_titik.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Unduh Tabel sebagai CSV",
            data=csv,
            file_name='titik_sampling.csv',
            mime='text/csv'
        )

        st.success("Perhitungan titik sampling selesai.")

    # Penjelasan rumus
    st.markdown(r"""
    ### 📐 Rumus Dasar

    Untuk metode equal area:

    $$
    r_i = R \cdot \sqrt{\frac{i - 0.5}{n}}
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

# Halaman Penjelasan & Informasi
elif halaman == "Penjelasan & Informasi 💡":
    st.title("Informasi Mengenai Sampling Emisi Tidak Bergerak")
    st.markdown("""
    ## Apa itu Sampling Emisi Tidak Bergerak?
    Sampling emisi tidak bergerak adalah proses pengambilan contoh gas buang dari sumber tetap, seperti cerobong industri, untuk dianalisis kandungan polutannya.

    ### Tujuan Sampling
    - Mengetahui konsentrasi polutan seperti SO₂, NOx, CO, NH₃, dan partikulat (TSP, PM10).
    - Menilai efisiensi alat pengendali polusi udara.
    - Memenuhi persyaratan peraturan pemerintah (SNI, Permen LH, USEPA).

    ### Metode
