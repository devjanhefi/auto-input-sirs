# Auto Input SIRS

Aplikasi otomatisasi input data berbasis web menggunakan Python dan Selenium.

## Deskripsi

Project ini dibuat untuk membantu mengurangi pekerjaan input data yang berulang dengan cara membaca data dari file Excel dan mengisikannya secara otomatis ke formulir web.

## Fitur

* Membaca data dari file Excel
* Mengisi formulir web secara otomatis
* Menggunakan browser Google Chrome yang sudah login
* Mengurangi kesalahan input manual
* Mempercepat proses pengisian data

## Teknologi

* Python
* Selenium
* Pandas
* Google Chrome

## Struktur File

```text
main.py
sample.xlsx
requirements.txt
README.md
```

## Instalasi

Install library yang dibutuhkan:

```bash
pip install -r requirements.txt
```

## Cara Menjalankan

### 1. Jalankan Chrome dalam mode debugging

Buka Command Prompt lalu jalankan:

```cmd
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeBot"
```

### 2. Login ke aplikasi web

Setelah Chrome terbuka, lakukan login ke aplikasi web yang akan digunakan.

### 3. Siapkan file Excel

Sesuaikan data pada file `sample.xlsx` dengan format yang dibutuhkan program.

### 4. Jalankan program

```bash
python main.py
```

## Screenshot

![Screenshot](screenshot.png)

## Catatan

Repository ini hanya berisi contoh implementasi otomatisasi menggunakan Selenium. Seluruh data, konfigurasi, dan informasi sensitif telah dihilangkan.
