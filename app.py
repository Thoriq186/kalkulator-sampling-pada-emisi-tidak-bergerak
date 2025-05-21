import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="Kalkulator Titik Sampling Isokinetik", layout="centered")

st.title("📏 Kalkulator kontol Sampling Emisi Tidak Bergerak")
st.caption("🔬 Berdasarkan Metode 1 - Isokinetik (Equal Area)")

# Input pengguna
st.subheader("🧮 Input Parameter")
col1, col2 = st.columns(2)
with col1:
    diameter = st.number_input("Diameter Cerobong (m)", min_value=0.1, step=0.01)
    upstream = st.number_input("Jarak Upstream dari Gangguan (m)", min_value=0.0, step=0.1)
with col2:
    panjang_nipple = st.number_input("Panjang Nipple (m)", min_value=0.0, step=0.1)
    downstream = st.number_input("Jarak Downstream dari Gangguan (m)", min_value=0.0, step=0.1)

hitung = st.button("🔍 Hitung Titik Sampling")

# Fungsi untuk menentukan jumlah titik lintas
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

# Tampilkan hasil jika tombol ditekan
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

    st.success("✅ Perhitungan selesai!")
    st.write(f"Jumlah titik lintas otomatis: **{jumlah_titik} titik**")
    st.dataframe(df, use_container_width=True)

    # Tombol unduh CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Unduh Tabel sebagai CSV",
        data=csv,
        file_name='titik_sampling.csv',
        mime='text/csv'
    )

# Penjelasan metode dalam expander
with st.expander("📖 Penjelasan Metode & Rumus"):
    st.markdown(r"""
    ### Rumus Equal Area:

    $$
    r_i = R \cdot \sqrt{\frac{i - 0.5}{n}} \\
    d_i = R - r_i
    $$

    **Keterangan:**
    - \( R \): Jari-jari cerobong (m)
    - \( i \): Nomor titik sampling
    - \( n \): Jumlah titik sampling
    - \( d_i \): Jarak dari dinding ke titik sampling ke-i

    **Sumber Regulasi:**
    - SNI 7117.13.2009
    - USEPA Method 1–5
    - Permen LH No. 13 Tahun 2009
    """)

st.markdown("---")
st.caption("📘 Aplikasi oleh [Metode Isokinetik EPA]. Dirancang untuk kemudahan teknisi lapangan.")
