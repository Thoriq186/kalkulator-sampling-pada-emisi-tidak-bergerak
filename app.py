import streamlit as st
import math
import pandas as pd

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Sampling Emisi Isokinetik", layout="centered")

# Judul Aplikasi
st.title("📏 Kalkulator Sampling Emisi Tidak Bergerak")
st.caption("🔬 Berdasarkan Metode 1 - Isokinetik (Equal Area)")

# Sidebar Navigasi
with st.sidebar:
    st.header("📂 Navigasi Halaman")
    halaman = st.radio("Pilih Halaman", ["Kalkulator Titik Sampling 🧮", "Penjelasan & Informasi 💡"])

# ---------------------- #
# Halaman Kalkulator
# ---------------------- #
if halaman == "Kalkulator Titik Sampling 🧮":
    st.subheader("🧮 Input Parameter Cerobong")

    col1, col2 = st.columns(2)
    with col1:
        diameter = st.number_input("Diameter Cerobong (m)", min_value=0.1, step=0.01)
        upstream = st.number_input("Jarak Upstream dari Gangguan (m)", min_value=0.0, step=0.1)
    with col2:
        panjang_nipple = st.number_input("Panjang Nipple (m)", min_value=0.0, step=0.1)
        downstream = st.number_input("Jarak Downstream dari Gangguan (m)", min_value=0.0, step=0.1)

    hitung = st.button("🔍 Hitung Titik Sampling")

    def tentukan_jumlah_titik(d, up, down):
        if d >= 0.61:
            if up >= 8 * d and down >= 2 * d:
                return 12
            elif up >= 4 * d and down >= 1 * d:
                return 10
            else:
                return 8
        elif 0.3 <= d < 0.61:
            return 8
        else:
            return 6

    if hitung and diameter:
        jumlah_titik = tentukan_jumlah_titik(diameter, upstream, downstream)
        radius = diameter / 2

        data_tabel = []
        for i in range(1, jumlah_titik + 1):
            posisi = radius * math.sqrt((i - 0.5) / jumlah_titik)
            jarak_tepi = round(radius - posisi, 4)
            jarak_pusat = round(posisi, 4)
            data_tabel.append({
                "Titik ke-": i,
                "Dari tepi (m)": jarak_tepi,
                "Dari pusat (m)": jarak_pusat
            })

        df = pd.DataFrame(data_tabel)

        st.success("✅ Perhitungan berhasil!")
        st.write(f"Jumlah titik lintas otomatis: **{jumlah_titik} titik**")
        st.dataframe(df, use_container_width=True)

        # Tombol download
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Unduh Tabel sebagai CSV",
            data=csv,
            file_name='titik_sampling.csv',
            mime='text/csv'
        )

    with st.expander("📖 Lihat Rumus dan Penjelasan Metode"):
        st.markdown(r"""
        ### Rumus Equal Area Sampling

        $$
        r_i = R \cdot \sqrt{\frac{i - 0.5}{n}}, \quad d_i = R - r_i
        $$

        **Keterangan:**
        - \( R \): Jari-jari cerobong (m)
        - \( i \): Nomor titik sampling ke-i
        - \( n \): Jumlah titik sampling
        - \( d_i \): Jarak dari dinding cerobong ke titik sampling ke-i
        """)

# ---------------------- #
# Halaman Penjelasan
# ---------------------- #
elif halaman == "Penjelasan & Informasi 💡":
    st.title("📘 Informasi Mengenai Sampling Emisi Tidak Bergerak")

    st.markdown("""
    ## Apa itu Sampling Emisi Tidak Bergerak?
    Sampling emisi tidak bergerak adalah proses pengambilan contoh gas buang dari sumber tetap, seperti cerobong industri, untuk dianalisis kandungan polutannya. Ini penting untuk mengevaluasi tingkat pencemaran udara dan kepatuhan terhadap regulasi lingkungan.

    ### Tujuan Sampling
    - Mengetahui konsentrasi polutan seperti **SO₂**, **NOx**, **CO**, **NH₃**, dan **partikulat (TSP, PM10)**.
    - Menilai efisiensi **alat pengendali polusi udara** (seperti scrubber, filter, ESP).
    - Memenuhi persyaratan **regulasi pemerintah**, seperti:
        - SNI 7117.13:2009
        - Permen LH No. 13 Tahun 2009
        - USEPA Method 1–5

    ---

    ## Metode Sampling Isokinetik
    - **Isokinetik** berarti kecepatan gas yang masuk ke probe sama dengan kecepatan gas di dalam cerobong.
    - Jika kecepatan tidak sesuai, maka hasil sampling bisa **terlalu banyak (over-sampling)** atau **terlalu sedikit (under-sampling)**.
    - Untuk menentukan titik pengambilan sampel, digunakan metode **equal area (pembagian luas penampang cerobong secara merata)**.

    **Rumus Titik Sampling:**

    $$
    r_i = R \cdot \sqrt{\frac{i - 0.5}{n}}, \quad d_i = R - r_i
    $$

    ---

    ## Persyaratan Penempatan Titik Sampling

    | Kondisi Aliran           | Upstream Minimum | Downstream Minimum | Jumlah Titik |
    |--------------------------|------------------|---------------------|--------------|
    | Ideal                    | ≥ 8D             | ≥ 2D                | 12 titik     |
    | Cukup Baik               | ≥ 4D             | ≥ 1D                | 10 titik     |
    | Tidak Ideal              | < 4D atau < 1D   |                     | 8 titik      |

    ---

    ## Standar dan Regulasi
    - **SNI 7117.13:2009** – Standar Indonesia pengukuran emisi partikulat
    - **USEPA Method 1–5** – Metode sampling cerobong di AS
    - **Permen LH No. 13 Tahun 2009** – Baku mutu emisi untuk sumber tidak bergerak
    """)

    st.info("ℹ️ Informasi ini ditujukan untuk teknisi, operator laboratorium, dan pengawas lingkungan.")
