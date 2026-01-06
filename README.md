# 📄 Aplikasi OCR Sederhana - Tugas Pengolahan Citra Digital

## 📋 Deskripsi
Aplikasi desktop untuk Optical Character Recognition (OCR) yang dibangun menggunakan Python, Tkinter, dan Tesseract OCR. Aplikasi ini dapat mengonversi teks dalam gambar menjadi teks digital dengan menampilkan tingkat akurasi.

## ✨ Fitur Utama
- 📸 **Buka berbagai format gambar** (JPG, PNG, BMP, JPEG)
- 🔍 **Proses OCR dengan preprocessing** untuk meningkatkan akurasi
- 📊 **Tampilkan persentase akurasi** dengan indikator warna
- 🌐 **Support multi-bahasa** (English dan Indonesia)
- 🛠️ **Preprocessing otomatis**: Grayscale, Denoising, Thresholding
- 📋 **Salin teks ke clipboard** dengan satu klik

## 🖼️ Screenshot Aplikasi
![Screenshot Aplikasi](screenshot.png)

## 🚀 Instalasi dan Penggunaan

### Prerequisites
- Python 3.7+
- Tesseract OCR

### 1. Install Tesseract OCR
**Windows:**
1. Download dari [UB-Mannheim Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Install dengan default settings
3. Pastikan path: `C:\Program Files\Tesseract-OCR\tesseract.exe`

**Install Python Libraries:**
```bash
pip install -r requirements.txt