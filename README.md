# 📄 Aplikasi OCR

## 📋 Deskripsi
Aplikasi desktop untuk Optical Character Recognition (OCR) yang dibangun menggunakan Python dan Tkinter. Aplikasi ini dapat membaca teks dari dalam gambar (JPG, PNG, BMP) dan mengonversinya menjadi teks digital, dilengkapi dengan informasi persentase akurasi.

## ✨ Fitur Utama
- 📸 **Membuka Berbagai Format Gambar**: JPG, JPEG, PNG, BMP
- 🔍 **Proses OCR dengan Preprocessing**: Meningkatkan akurasi dengan konversi grayscale, denoising, dan thresholding
- 📊 **Menampilkan Akurasi**: Persentase kepercayaan hasil OCR dengan indikator warna (hijau/oranye/merah)
- 🌐 **Multi-bahasa**: Mendukung bahasa Inggris (`eng`) dan Indonesia (`ind`)
- 🛠️ **Antarmuka Pengguna Sederhana**: Dibangun dengan Tkinter, mudah digunakan
- 📋 **Fungsi Praktis**: Salin teks ke clipboard, hapus hasil, reset aplikasi

## 🚀 Panduan Instalasi & Menjalankan

### Persyaratan
1. **Python 3.7 atau lebih tinggi** - [Download Python](https://www.python.org/downloads/)
2. **Tesseract OCR Engine** - Wajib diinstal di sistem
    - **Windows**: Unduh dari [UB-Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
    - **Linux (Ubuntu/Debian)**: `sudo apt install tesseract-ocr`
    - **macOS**: `brew install tesseract`

### Langkah 1: Clone/Download Project
Download seluruh folder project ke komputer kamu.

### Langkah 2: Instal Library Python
Buka terminal atau command prompt di dalam folder project, lalu jalankan perintah:
```bash
pip install -r requirements.txt
```
File `requirements.txt` berisi:
```txt
Pillow==10.0.0
pytesseract==0.3.10
opencv-python==4.8.1.78
numpy==1.24.3
```

### Langkah 3: Verifikasi Path Tesseract (Khusus Windows)
Buka file `ocr_app.py`, pastikan baris berikut mengarah ke lokasi `tesseract.exe` yang benar di komputer kamu:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### Langkah 4: Menjalankan Aplikasi
Di terminal dalam folder project, jalankan:
```bash
python ocr_app.py
```
Aplikasi akan terbuka.

## 📖 Cara Penggunaan
1.  **Buka Gambar**: Klik tombol `📂 Buka Gambar`, pilih file gambar (.jpg, .png, .bmp).
2.  **Atur Pengaturan** (Opsional): Pilih bahasa OCR dan aktifkan/nonaktifkan opsi preprocessing di panel kanan.
3.  **Proses OCR**: Klik tombol `🔍 Proses OCR`. Teks hasil akan muncul di panel kanan beserta persentase akurasinya.
4.  **Salin atau Hapus Hasil**: Gunakan tombol `📋 Salin Teks` atau `🗑️ Hapus Hasil` untuk mengelola teks.
