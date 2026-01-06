import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageOps
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi OCR")
        self.root.geometry("900x600")
        self.root.configure(bg="#f5f5f5")
        
        self.image_path = None
        self.original_image = None
        
        # Header
        header_frame = tk.Frame(root, bg="#4CAF50", height=60)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="📄 APLIKASI OCR",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 16, "bold")
        ).pack(expand=True, pady=15)
        
        # Main Content
        main_frame = tk.Frame(root, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left Panel - Image
        left_frame = tk.LabelFrame(
            main_frame,
            text="Gambar",
            font=("Arial", 11, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Button Frame
        btn_frame = tk.Frame(left_frame, bg="white")
        btn_frame.pack(pady=5)
        
        tk.Button(
            btn_frame,
            text="📂 Buka Gambar",
            bg="#2196F3",
            fg="white",
            font=("Arial", 10),
            width=15,
            command=self.open_image
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="🔍 Proses OCR",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10),
            width=15,
            command=self.do_ocr
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="🔄 Reset",
            bg="#FF9800",
            fg="white",
            font=("Arial", 10),
            width=15,
            command=self.reset_all
        ).pack(side=tk.LEFT, padx=5)
        
        # Image Display
        self.image_label = tk.Label(
            left_frame,
            bg="#e0e0e0",
            relief="solid",
            bd=1,
            text="Gambar akan muncul di sini\n\nUkuran maks: 400x400",
            font=("Arial", 9),
            compound=tk.CENTER,
            wraplength=350
        )
        self.image_label.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Image Info
        self.info_label = tk.Label(
            left_frame,
            text="Belum ada gambar",
            bg="white",
            fg="#666666",
            font=("Arial", 9)
        )
        self.info_label.pack()
        
        # Right Panel - Results
        right_frame = tk.LabelFrame(
            main_frame,
            text="Hasil OCR",
            font=("Arial", 11, "bold"),
            bg="white",
            padx=10,
            pady=10
        )
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Results Header
        result_header = tk.Frame(right_frame, bg="white")
        result_header.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            result_header,
            text="Teks yang terdeteksi:",
            bg="white",
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT)
        
        self.accuracy_label = tk.Label(
            result_header,
            text="Akurasi: -",
            bg="white",
            fg="#4CAF50",
            font=("Arial", 10)
        )
        self.accuracy_label.pack(side=tk.RIGHT)
        
        # Text Area with Scrollbar
        text_frame = tk.Frame(right_frame, bg="white")
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.text_area = tk.Text(
            text_frame,
            wrap=tk.WORD,
            font=("Arial", 10),
            height=20,
            bg="#fafafa",
            relief="solid",
            yscrollcommand=scrollbar.set
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text_area.yview)
        
        # Control Buttons for Results
        control_frame = tk.Frame(right_frame, bg="white")
        control_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            control_frame,
            text="📋 Salin Teks",
            bg="#607D8B",
            fg="white",
            font=("Arial", 9),
            command=self.copy_text
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            control_frame,
            text="🗑️ Hapus Hasil",
            bg="#F44336",
            fg="white",
            font=("Arial", 9),
            command=self.clear_results
        ).pack(side=tk.LEFT, padx=2)
        
        # Settings Panel
        settings_frame = tk.LabelFrame(
            right_frame,
            text="Pengaturan",
            font=("Arial", 10),
            bg="white",
            padx=10,
            pady=10
        )
        settings_frame.pack(fill=tk.X, pady=(10, 0))
        
        # Language selection
        lang_frame = tk.Frame(settings_frame, bg="white")
        lang_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(lang_frame, text="Bahasa:", bg="white").pack(side=tk.LEFT)
        self.lang_var = tk.StringVar(value="eng")
        lang_combo = ttk.Combobox(
            lang_frame,
            textvariable=self.lang_var,
            values=["eng", "ind", "eng+ind"],
            width=12,
            state="readonly"
        )
        lang_combo.pack(side=tk.RIGHT)
        
        # Preprocessing options
        tk.Label(settings_frame, text="Preprocessing:", bg="white", font=("Arial", 9)).pack(anchor=tk.W, pady=(5, 0))
        
        self.denoise_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            settings_frame,
            text="Hilangkan noise",
            variable=self.denoise_var,
            bg="white"
        ).pack(anchor=tk.W)
        
        self.threshold_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            settings_frame,
            text="Thresholding",
            variable=self.threshold_var,
            bg="white"
        ).pack(anchor=tk.W)
        
        # Footer
        footer = tk.Label(
            root,
            text="Aplikasi OCR Sederhana © 2024",
            bg="#333333",
            fg="white",
            font=("Arial", 9),
            pady=5
        )
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        
    def open_image(self):
        """Open and display image"""
        file_path = filedialog.askopenfilename(
            title="Pilih gambar",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return
        
        self.image_path = file_path
        self.original_image = cv2.imread(file_path)
        
        # Display image
        self.display_image(self.original_image)
        
        # Update info
        img = Image.open(file_path)
        width, height = img.size
        self.info_label.config(
            text=f"Ukuran: {width}x{height} | Format: {file_path.split('.')[-1].upper()}"
        )
    
    def display_image(self, image):
        """Display image in label"""
        if len(image.shape) == 3:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        else:
            image_rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        
        pil_img = Image.fromarray(image_rgb)
        
        # Resize if too big
        max_size = 400
        if pil_img.width > max_size or pil_img.height > max_size:
            pil_img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        self.tk_img = ImageTk.PhotoImage(pil_img)
        self.image_label.config(image=self.tk_img, text="")
    
    def preprocess_image(self, image):
        """Apply preprocessing to improve OCR accuracy"""
        # Convert to grayscale
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # Denoising
        if self.denoise_var.get():
            gray = cv2.medianBlur(gray, 3)
        
        # Thresholding
        if self.threshold_var.get():
            _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        return gray
    
    def do_ocr(self):
        """Perform OCR on the image"""
        if not self.image_path:
            messagebox.showwarning("Peringatan", "Silakan pilih gambar terlebih dahulu!")
            return
        
        try:
            # Read and preprocess image
            img = cv2.imread(self.image_path)
            processed_img = self.preprocess_image(img)
            
            # Display processed image
            self.display_image(processed_img)
            
            # Perform OCR
            lang = self.lang_var.get()
            custom_config = r'--oem 3 --psm 6'
            
            # Get text with confidence
            data = pytesseract.image_to_data(
                processed_img, 
                lang=lang, 
                config=custom_config,
                output_type=pytesseract.Output.DICT
            )
            
            # Extract text
            text = pytesseract.image_to_string(processed_img, lang=lang, config=custom_config)
            
            # Calculate accuracy
            confidences = [int(conf) for conf in data['conf'] if int(conf) > 0]
            if confidences:
                accuracy = sum(confidences) / len(confidences)
                accuracy_text = f"Akurasi: {accuracy:.1f}%"
                color = "#4CAF50" if accuracy > 70 else "#FF9800" if accuracy > 50 else "#F44336"
            else:
                accuracy_text = "Akurasi: Tidak terdeteksi"
                color = "#F44336"
                accuracy = 0
            
            # Update UI
            self.accuracy_label.config(text=accuracy_text, fg=color)
            
            # Display results
            self.text_area.delete(1.0, tk.END)
            if text.strip():
                self.text_area.insert(tk.END, text)
                if accuracy > 0:
                    self.text_area.insert(tk.END, f"\n\n{'='*40}\nAkurasi: {accuracy:.1f}%")
            else:
                self.text_area.insert(tk.END, "Tidak ada teks yang terdeteksi.")
            
            # Show success message
            if text.strip():
                messagebox.showinfo(
                    "Sukses", 
                    f"OCR selesai!\n\n"
                    f"Teks berhasil dibaca dengan akurasi {accuracy:.1f}%\n"
                    f"Panjang teks: {len(text)} karakter"
                )
            else:
                messagebox.showwarning("Peringatan", "Tidak ada teks yang terdeteksi pada gambar.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
    
    def copy_text(self):
        """Copy text to clipboard"""
        text = self.text_area.get(1.0, tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("Sukses", "Teks berhasil disalin ke clipboard!")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada teks untuk disalin.")
    
    def clear_results(self):
        """Clear OCR results"""
        self.text_area.delete(1.0, tk.END)
        self.accuracy_label.config(text="Akurasi: -", fg="#4CAF50")
    
    def reset_all(self):
        """Reset everything"""
        self.image_path = None
        self.original_image = None
        self.image_label.config(
            image="",
            text="Gambar akan muncul di sini\n\nUkuran maks: 400x400"
        )
        self.info_label.config(text="Belum ada gambar")
        self.clear_results()
        messagebox.showinfo("Reset", "Semua data telah direset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()