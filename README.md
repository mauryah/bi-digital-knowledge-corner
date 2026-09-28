# BI Digital Knowledge Corner v2

## Isi
- `app.py` — aplikasi Streamlit
- `requirements.txt` — dependency
- `data/feedback_template.csv` — template kolom feedback
- `README.md` — panduan tahap pengerjaan

## Jalankan lokal
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Jalankan di Google Colab
```python
!pip install -q streamlit pandas
!streamlit run app.py &>/content/streamlit.log &
```
Untuk demo publik, deploy ke Streamlit Community Cloud atau gunakan tunneling yang tersedia di lingkungan Anda.

## Tahapan proyek
1. Observasi masalah layanan informasi.
2. Tentukan target pengguna dan scope.
3. Kurasi materi dari sumber resmi BI.
4. Bangun prototype Streamlit.
5. Hubungkan URL katalog/aplikasi perpustakaan yang benar.
6. Deploy dan buat QR Code.
7. Uji coba 20–30 pengguna (atau sesuai arahan pembimbing).
8. Kumpulkan feedback.
9. Analisis hasil dan dampak.
10. Masukkan hasil ke BAB I–V.

## Pengukuran
Gunakan indikator: kemudahan penggunaan, kemudahan menemukan informasi, kemudahan memahami, manfaat, tampilan, dan rekomendasi. Gunakan data nyata; jangan menjadikan angka contoh sebagai hasil penelitian.

## Penting
Prototype bukan aplikasi resmi BI. Verifikasi konten, tautan, identitas visual, dan izin penggunaan sebelum dipakai secara resmi.
