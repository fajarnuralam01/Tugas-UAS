import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- 1. Konfigurasi Halaman ---
st.set_page_config(
    page_title="Bike Sharing Dashboard - Kelompok 2",
    page_icon="🚲",
    layout="wide"
)

# --- 2. Load Data ---
@st.cache_data
def load_data():
    try:
        # Pastikan file ini ada di folder yang sama
        day_df = pd.read_csv("day.csv")
        hour_df = pd.read_csv("hour.csv")
        
        # Konversi Tanggal
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
        
        # Mapping Label agar mudah dibaca
        season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
        weather_map = {1: 'Cerah/Berawan', 2: 'Mendung/Berkabut', 3: 'Hujan Ringan/Salju', 4: 'Hujan Lebat/Badai'}
        weekday_map = {0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'}
        month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 
                     7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}

        day_df['season_label'] = day_df['season'].map(season_map)
        day_df['weathersit_label'] = day_df['weathersit'].map(weather_map)
        day_df['weekday_label'] = day_df['weekday'].map(weekday_map)
        day_df['month_label'] = day_df['mnth'].map(month_map)
        
        hour_df['season_label'] = hour_df['season'].map(season_map)
        
        return day_df, hour_df
    except FileNotFoundError:
        return None, None

day_df, hour_df = load_data()

if day_df is None:
    st.error("⚠️ File 'day.csv' dan 'hour.csv' tidak ditemukan! Pastikan file ada di folder yang sama di GitHub.")
    st.stop()

# --- 3. Sidebar (Profil & Filter) ---
with st.sidebar:
    st.title("🚲 Bike Sharing Info")
    st.header("Kelompok 2 (IF-1)")
    st.markdown("""
    **Anggota Tim:**
    1. Adrian Mulya Wijaya (10124016)
    2. Muhammad Rifky Sandi Yudha (10124027)
    3. Rizki Mardiansyah (10124036)
    4. Rafi Faris Faizi (10124038)
    5. Fajar Nur Alam (10124039)
    6. Joao Vong Tavares (10124480)
    """)
    
    st.markdown("---")
    st.subheader("Filter Data")
    
    # Filter Rentang Waktu
    min_date = day_df['dteday'].min()
    max_date = day_df['dteday'].max()
    
    start_date, end_date = st.date_input(
        "Pilih Rentang Waktu:",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# Filter Data Utama
main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                 (day_df['dteday'] <= pd.to_datetime(end_date))]

# --- 4. Main Content ---
st.title("📊 Dashboard Analisis Penyewaan Sepeda")
st.markdown("Dashboard ini menampilkan hasil analisis dari **12 Pertanyaan Bisnis** yang diajukan oleh tim.")

# KPI Utama
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Penyewaan", value=f"{main_df['cnt'].sum():,}")
with col2:
    st.metric("Rata-rata Harian", value=f"{main_df['cnt'].mean():.0f}")
with col3:
    st.metric("Pengguna Registered", value=f"{main_df['registered'].sum():,}")
with col4:
    st.metric("Pengguna Casual", value=f"{main_df['casual'].sum():,}")

st.markdown("---")

# --- 5. Tabs (Navigasi 12 Pertanyaan) ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Tren & Waktu", 
    "⏰ Pola Jam & Hari", 
    "🌤️ Faktor Cuaca", 
    "👥 Segmentasi Pengguna",
    "🔍 Advanced (Clustering)"
])

# === TAB 1: TREN & WAKTU (Adrian & Joao) ===
with tab1:
    st.header("Analisis Tren & Waktu")
    
    # Q1: Tren Tahunan (Adrian)
    st.subheader("1. Tren Penyewaan Tahunan (Adrian)")
    fig_trend, ax_trend = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=main_df, x='dteday', y='cnt', color='#1f77b4', ax=ax_trend)
    ax_trend.set_title("Grafik Tren Harian")
    st.pyplot(fig_trend)
    
    col_a, col_b = st.columns(2)
    with col_a:
        # Q11: Pola Bulanan (Joao)
        st.subheader("2. Pola Bulanan (Joao)")
        monthly_avg = main_df.groupby('mnth')['cnt'].mean().reset_index()
        fig_month, ax_month = plt.subplots()
        sns.barplot(data=monthly_avg, x='mnth', y='cnt', palette='Blues_d', ax=ax_month)
        ax_month.set_xlabel("Bulan (1-12)")
        st.pyplot(fig_month)
        
    with col_b:
        # Q8: Distribusi Weekday (Rafi)
        st.subheader("3. Distribusi Hari (Rafi)")
        weekday_avg = main_df.groupby('weekday')['cnt'].mean().reset_index()
        fig_day, ax_day = plt.subplots()
        sns.barplot(data=weekday_avg, x='weekday', y='cnt', palette='Greens_d', ax=ax_day)
        ax_day.set_xlabel("Hari (0=Minggu, 6=Sabtu)")
        st.pyplot(fig_day)

# === TAB 2: POLA JAM & HARI (Rifky) ===
with tab2:
    st.header("Pola Jam & Aktivitas Harian")
    
    # Q3: Peak Hours (Rifky)
    st.subheader("1. Jam Sibuk (Peak Hours) - (Rifky)")
    hourly_avg = hour_df.groupby('hr')['cnt'].mean().reset_index()
    fig_hour, ax_hour = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=hourly_avg, x='hr', y='cnt', marker='o', color='red', ax=ax_hour)
    ax_hour.set_xticks(range(0, 24))
    ax_hour.set_title("Rata-rata Penyewaan per Jam")
    ax_hour.grid(True)
    st.pyplot(fig_hour)
    
    # Q4: Workingday vs Holiday (Rifky)
    st.subheader("2. Hari Kerja vs Libur - (Rifky)")
    fig_work, ax_work = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=main_df, x='workingday', y='cnt', palette='Set2', ax=ax_work)
    ax_work.set_xticklabels(['Libur/Akhir Pekan', 'Hari Kerja'])
    st.pyplot(fig_work)

# === TAB 3: FAKTOR CUACA & MUSIM (Rizki, Adrian, Rafi, Fajar) ===
with tab3:
    st.header("Analisis Faktor Alam")
    
    col_c, col_d = st.columns(2)
    with col_c:
        # Q5: Musim Terbaik (Rizki)
        st.subheader("1. Musim Teramai (Rizki)")
        fig_sea, ax_sea = plt.subplots()
        sns.barplot(data=main_df, x='season_label', y='cnt', estimator=sum, palette='autumn', ax=ax_sea)
        st.pyplot(fig_sea)
        
        # Q2: Korelasi Suhu (Adrian)
        st.subheader("2. Korelasi Suhu (Adrian)")
        fig_temp, ax_temp = plt.subplots()
        sns.scatterplot(data=main_df, x='temp', y='cnt', hue='season_label', alpha=0.6, ax=ax_temp)
        st.pyplot(fig_temp)
        
    with col_d:
        # Q7: Cuaca Ekstrem (Rafi)
        st.subheader("3. Dampak Cuaca (Rafi)")
        fig_weath, ax_weath = plt.subplots()
        sns.boxplot(data=main_df, x='weathersit_label', y='cnt', palette='cool', ax=ax_weath)
        st.pyplot(fig_weath)
        
        # Q6 & Q10: Kelembaban & Angin (Rizki & Fajar)
        st.subheader("4. Kelembaban & Angin (Rizki & Fajar)")
        tab_sub1, tab_sub2 = st.tabs(["Kelembaban", "Kecepatan Angin"])
        with tab_sub1:
            fig_hum, ax_hum = plt.subplots()
            sns.scatterplot(data=main_df, x='hum', y='cnt', color='teal', alpha=0.5, ax=ax_hum)
            st.pyplot(fig_hum)
        with tab_sub2:
            fig_wind, ax_wind = plt.subplots()
            sns.scatterplot(data=main_df, x='windspeed', y='cnt', color='purple', alpha=0.5, ax=ax_wind)
            st.pyplot(fig_wind)

# === TAB 4: SEGMENTASI PENGGUNA (Fajar & Joao) ===
with tab4:
    st.header("Analisis Tipe Pengguna")
    
    col_e, col_f = st.columns(2)
    with col_e:
        # Q9: Proporsi Pengguna (Fajar)
        st.subheader("1. Registered vs Casual (Fajar)")
        total_casual = main_df['casual'].sum()
        total_registered = main_df['registered'].sum()
        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie([total_casual, total_registered], labels=['Casual', 'Registered'], autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
        st.pyplot(fig_pie)
        
    with col_f:
        # Q12: Pola Jam per Tipe (Joao)
        st.subheader("2. Pola Jam per Tipe User (Joao)")
        hourly_user = hour_df.groupby('hr')[['casual', 'registered']].mean().reset_index()
        fig_user, ax_user = plt.subplots()
        ax_user.plot(hourly_user['hr'], hourly_user['casual'], label='Casual', marker='o')
        ax_user.plot(hourly_user['hr'], hourly_user['registered'], label='Registered', marker='o')
        ax_user.legend()
        ax_user.set_xlabel("Jam")
        ax_user.grid(True)
        st.pyplot(fig_user)

# === TAB 5: DATA MINING (CLUSTERING) ===
with tab5:
    st.header("🔍 Advanced Analysis: Clustering")
    st.markdown("""
    Analisis ini menggunakan **K-Means Clustering** untuk mengelompokkan hari berdasarkan kondisi cuaca
    (Temperatur, Kelembaban, Kecepatan Angin) untuk melihat pola penyewaan.
    """)
    
    # Slider untuk memilih jumlah cluster
    num_clusters = st.slider("Jumlah Cluster:", 2, 5, 3)
    
    # Data preprocessing
    X = main_df[['temp', 'hum', 'windspeed']].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Modeling
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    main_df['cluster'] = kmeans.fit_predict(X_scaled)
    
    # Visualisasi Scatter Plot
    fig_cluster, ax_cluster = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=main_df, x='temp', y='hum', 
        hue='cluster', size='cnt', sizes=(50, 300), 
        palette='viridis', ax=ax_cluster
    )
    ax_cluster.set_title(f"Clustering Hari (Cluster {num_clusters})")
    ax_cluster.set_xlabel("Temperatur (Normalized)")
    ax_cluster.set_ylabel("Kelembaban (Normalized)")
    st.pyplot(fig_cluster)
    
    st.caption("Semakin besar titik, semakin banyak penyewaan sepeda.")

st.caption("Copyright © Kelompok 2 - IF-1")
