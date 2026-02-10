import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# --- Judul Dashboard ---
st.title("🚲 Bike Sharing Analytics Dashboard")
st.markdown("Dashboard ini menganalisis performa penyewaan sepeda, pola musiman, dan klasterisasi cuaca.")

# --- Load Data ---
# Cache data agar dashboard tidak lambat saat reload
@st.cache_data
def load_data():
    # Pastikan file day.csv dan hour.csv ada di folder yang sama nanti di GitHub
    # Kita gunakan try-except agar tidak error saat belum ada file
    try:
        day_df = pd.read_csv("day.csv")
        hour_df = pd.read_csv("hour.csv")
        
        # Cleaning sederhana untuk dashboard
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
        
        # Mapping label musim
        season_map = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
        day_df['season_label'] = day_df['season'].map(season_map)
        
        return day_df, hour_df
    except FileNotFoundError:
        return None, None

day_df, hour_df = load_data()

if day_df is None:
    st.error("File dataset tidak ditemukan. Pastikan day.csv dan hour.csv ada di direktori yang sama.")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    "Rentang Waktu",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter dataset berdasarkan tanggal
main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                 (day_df['dteday'] <= pd.to_datetime(end_date))]

# --- Metric Utama ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", value=main_df['cnt'].sum())
with col2:
    st.metric("Rata-rata Harian", value=f"{main_df['cnt'].mean():.2f}")
with col3:
    st.metric("Hari Teramai", value=main_df.loc[main_df['cnt'].idxmax(), 'dteday'].strftime('%Y-%m-%d'))

# --- Visualisasi 1: Tren Penyewaan ---
st.subheader("📈 Tren Penyewaan Sepeda Harian")
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(main_df['dteday'], main_df['cnt'], marker='o', markersize=2, color="#90CAF9")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# --- Visualisasi 2: Analisis Musim & Cuaca ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("🌤️ Penyewaan Berdasarkan Musim")
    fig_season, ax_season = plt.subplots()
    sns.barplot(x="season_label", y="cnt", data=main_df, estimator=sum, errorbar=None, ax=ax_season, palette="coolwarm")
    ax_season.set_ylabel("Total Sewa")
    st.pyplot(fig_season)

with col_b:
    st.subheader("⏰ Pola Jam Sibuk")
    hourly_trend = hour_df.groupby("hr")["cnt"].mean().reset_index()
    fig_hour, ax_hour = plt.subplots()
    sns.lineplot(x="hr", y="cnt", data=hourly_trend, ax=ax_hour, color="#FF5722")
    ax_hour.set_xticks(range(0, 24))
    ax_hour.set_xlabel("Jam")
    ax_hour.set_ylabel("Rata-rata Sewa")
    st.pyplot(fig_hour)

# --- Visualisasi 3: Data Mining (K-Means Clustering) ---
st.subheader("🔍 Advanced Analysis: Clustering Kondisi Cuaca")
st.markdown("Menggunakan **K-Means Clustering** (Unsupervised Learning) untuk mengelompokkan hari berdasarkan cuaca.")

# Fitur untuk clustering
X_cluster = main_df[['temp', 'hum', 'windspeed']].copy()
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

# K-Means
num_clusters = st.slider("Jumlah Cluster", 2, 5, 3)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
main_df['cluster'] = kmeans.fit_predict(X_scaled)

# Plot Clustering
fig_cluster, ax_cluster = plt.subplots(figsize=(10, 6))
scatter = sns.scatterplot(
    data=main_df, 
    x='temp', 
    y='hum', 
    hue='cluster', 
    size='cnt', 
    sizes=(20, 200), 
    palette='viridis', 
    ax=ax_cluster
)
ax_cluster.set_xlabel("Temperatur (Normalized)")
ax_cluster.set_ylabel("Kelembaban (Normalized)")
ax_cluster.set_title(f"Clustering Cuaca (Cluster {num_clusters})")
st.pyplot(fig_cluster)

st.caption("Copyright © Kelompok 2 - IF-1")
