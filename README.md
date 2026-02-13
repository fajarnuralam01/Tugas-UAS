# UAS Pemprograman Dasar Sains Data

---
# Bike Sharing Dashboard
Dashboard ini dibangun untuk menganalisis data penyewaan sepeda (*Bike Sharing System*) guna memberikan wawasan bisnis strategis bagi pengambil keputusan.
Analisis mencakup tren waktu, pola operasional, dampak cuaca, segmentasi pelanggan, hingga penerapan *Advanced Analytics* seperti *Clustering* dan *Forecasting*.

---

# Identitas Kelompok
- **Kelompok 10124039**
- **Kelas** : IF-1
- **Anggota** :
  - Adrian Mulya Wijaya (10124016)<br>
    (Fokus Analisis: Tren & Suhu
     - Pertanyaan 1: Analisis performa penyewaan sepeda dalam beberapa tahun terakhir (Tren meningkat/menurun).
     - Pertanyaan 2: Analisis korelasi antara suhu (temp) dengan jumlah penyewaan.
     - Bekerja sama dalam tim membangun  Advanced Analytics
     - Bekerja sama dalam tim membangun Data Engineering (Penyedia Data)
     - Bekerja sama dalam tim membangun Deployment & Dashboard (Integrasi))
    
  - Muhammad Rifky Sandi Yudha (10124027)<br>
    (Fokus Analisis: Jam Operasional & Hari Kerja
     Pertanyaan 3: Identifikasi jam lonjakan permintaan (peak hours) tertinggi dan terendah.
     Pertanyaan 4: Analisis perbedaan pola penyewaan antara hari kerja (workingday) vs hari
     - Bekerja sama dalam tim membangun  Advanced Analytics
     - Bekerja sama dalam tim membangun Data Engineering (Penyedia Data)
     - Bekerja sama dalam tim membangun Deployment & Dashboard (Integrasi))
    
  - Rizki Mardiansyah (10124036)<br>
    (Fokus Analisis: Musim & Kelembaban
     Pertanyaan 5: Identifikasi musim dengan tingkat penyewaan tertinggi untuk acuan promosi.
     Pertanyaan 6: Analisis pengaruh kelembaban udara (humidity) terhadap penyewaan.
     - Bekerja sama dalam tim membangun  Advanced Analytics
     - Bekerja sama dalam tim membangun Data Engineering (Penyedia Data)
     - Bekerja sama dalam tim membangun Deployment & Dashboard (Integrasi))
    
  - Rafi Faris Faizi (10124038)<br>
    (Fokus Analisis: Cuaca Ekstrem & Pola Mingguan
     Pertanyaan 7: Analisis pengaruh kondisi cuaca ekstrem (hujan/salju) terhadap penurunan penyewaan.
     Pertanyaan 8: Analisis distribusi penyewaan berdasarkan hari dalam seminggu (weekday).
     - Bekerja sama dalam tim membangun  Advanced Analytics
     - Bekerja sama dalam tim membangun Data Engineering (Penyedia Data)
     - Bekerja sama dalam tim membangun Deployment & Dashboard (Integrasi))
       
  - Fajar Nur Alam (10124039)<br>
    (Fokus Analisis: Tipe User & Angin
     Pertanyaan 9: Perbandingan proporsi pengguna Registered vs Casual.
     Pertanyaan 10: Analisis pengaruh kecepatan angin (windspeed) terhadap jumlah penyewaan.
     - Bekerja sama dalam tim membangun  Advanced Analytics
     - Bekerja sama dalam tim membangun Data Engineering (Penyedia Data)
     - Bekerja sama dalam tim membangun Deployment & Dashboard (Integrasi))
    
  - Joao Vong Tavares Da Silva (10124480)<br>
    (Fokus Analisis: Pola Bulanan & Perilaku User
     Pertanyaan 11: Analisis pola penyewaan bulanan dan identifikasi bulan tersepi.
     Pertanyaan 12: Analisis perbandingan pola jam penggunaan antara Casual vs Registered.
     - Bekerja sama dalam tim membangun  Advanced Analytics
     - Bekerja sama dalam tim membangun Data Engineering (Penyedia Data)
     - Bekerja sama dalam tim membangun Deployment & Dashboard (Integrasi))
    
---

# Tampilan Dashboard

<img width="925" height="420" alt="{441E45D5-47EE-4399-846C-127B1645CD95}" src="https://github.com/user-attachments/assets/221a3398-6b82-4968-a907-0b963e165f67" />


# Link Dashboard
  - **Streamlit** : https://tugas-uas-q4wko9vqfpqxrkpqtxzlqu.streamlit.app/

# Penjelasan
  - **Youtube**   : https://youtu.be/dFyN7Bfv_wA

---

# Pertanyaan Analisis

Dashboard ini menjawab *12 Pertanyaan Bisnis* krusial :

1.  *Tren Tahunan:* Bagaimana performa pertumbuhan bisnis dari 2011 ke 2012?
2.  *Suhu:* Seberapa kuat korelasi suhu terhadap jumlah penyewaan?
3.  *Jam Sibuk:* Kapan waktu tersibuk (*Peak Hours*) untuk operasional?
4.  *Hari Kerja:* Apakah pengguna lebih aktif di hari kerja atau libur?
5.  *Musim:* Musim apa yang paling menguntungkan (*Highest Demand*)?
6.  *Kelembaban:* Bagaimana pengaruh kelembaban udara terhadap kenyamanan?
7.  *Cuaca Ekstrem:* Seberapa besar penurunan saat hujan/salju?
8.  *Hari Terbaik:* Hari apa dalam seminggu yang paling ramai?
9.  *Tipe User:* Berapa proporsi antara Member (*Registered*) vs Turis (*Casual*)?
10. *Angin:* Apakah kecepatan angin mempengaruhi keselamatan bersepeda?
11. *Pola Bulanan:* Bulan apa yang harus dihindari untuk promosi (*Low Season*)?
12. *Perilaku User:* Bagaimana beda pola jam main antara Member dan Casual?
    
---

# Tahapan Analisis Data

![WhatsApp Image 2026-02-13 at 17 16 05](https://github.com/user-attachments/assets/513a4155-e383-4dad-b14b-1e5e41b6931d)


1. *Menentukan Pertanyaan Bisnis (Ask)* :
   Merumuskan 12 pertanyaan kunci terkait tren pertumbuhan, pola operasional, dampak cuaca, dan perilaku pengguna untuk meningkatkan strategi bisnis.
   
2. *Menyiapkan Data (Prepare)* :
   Mengumpulkan dataset Bike Sharing (day.csv & hour.csv) serta menyiapkan library Python (pandas, matplotlib, seaborn, folium, sklearn) untuk analisis.]
  
3. *Memproses Data (Process)* :
   Membersihkan data dengan menangani *missing values*, mengubah tipe data tanggal (*datetime*), dan melakukan mapping label (musim, cuaca, hari) agar mudah diinterpretasi.

4. *Exploratory Data Analysis (Analyze):*
   Menganalisis data secara statistik dan visual untuk menjawab pertanyaan bisnis, serta menerapkan teknik lanjutan:
    - *Clustering*  : Mengelompokkan hari terbaik (Golden Days).
    - *Forecasting* : Memprediksi tren masa depan.
    - *Geoanalysis* : Memetakan lokasi operasional strategis.


5. *Visualisasi & Dashboard (Share)* :
   Membangun dashboard interaktif berbasis *Streamlit* dengan fitur filter tanggal dan tab navigasi (Tren, Operasional, Cuaca, User, Advanced) untuk penyajian data yang efektif.
   
6. *Kesimpulan & Rekomendasi (Act)* :
Menyusun strategi bisnis berdasarkan insight: fokus pada retensi member, optimasi stok di jam sibuk, dan mitigasi risiko operasional saat cuaca buruk.

---

# Library yang Di gunakan

1. streamlit
2. pandas
3. matplotlib
4. seaborn
5. scikit-learn
6. numpy
7. folium
8. streamlit-folium

---

# Struktur Repository

├── dashboard.jpeg        #Screenshot Dashboard<br>
├── dashboard UAS.py      # File utama untuk menjalankan Dashboard Streamlit<br>
├── day.csv               # Dataset harian (sumber data utama)<br>
├── hour.csv              # Dataset per jam (sumber data untuk analisis jam)<br>
├── IF1_Kelompok2.ipynb   # File Jupyter Notebook (tempat proses analisis data)<br>
├── requirements.txt      # Daftar library Python yang dibutuhkan (pip install)<br>
└── README.md             # Dokumentasi lengkap proyek

---
