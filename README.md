## Anggota Kelompok
- Pryta Rosela (2208107010046)
- Widya Nurul Sukma (2208107010054)
- Mila Lestari (2208107010002)

# Sistem Manajemen Produk

## Deskripsi Proyek
Proyek ini adalah sistem manajemen produk sederhana yang dibangun menggunakan Django. Sistem ini memungkinkan pengguna untuk melakukan operasi CRUD (Create, Read, Update, Delete) pada data produk.

## Fitur
- Form untuk menambahkan produk baru
- Halaman daftar produk
- Detail produk
- Edit produk
- Hapus produk
- Notifikasi flash message untuk setiap operasi yang berhasil

## Prasyarat
- Python 3.8 atau lebih baru
- Django 4.0 atau lebih baru

## Cara Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/WidyaNurulSukma/Tugas8_Kelompok8.git
cd Tugas8_Kelompok8
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
```

### 3. Aktifkan Virtual Environment
Untuk Windows:
```bash
venv\Scripts\activate
```

Untuk macOS dan Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Migrasi Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Buat Superuser (Opsional)
```bash
python manage.py createsuperuser
```

### 7. Jalankan Server Development
```bash
python manage.py runserver
```

Setelah server berjalan, akses aplikasi melalui web browser di http://127.0.0.1:8000/produk/

## Struktur Project
```
project_produk/
│
├── project_produk/      # Folder project utama
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── produk/              # Aplikasi produk
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py        # Definisi model Produk
│   ├── forms.py         # Form untuk produk
│   ├── views.py         # Logic untuk CRUD
│   ├── urls.py          # Routing aplikasi
│   ├── migrations/
│   └── templates/       # Template HTML
│       └── produk/
│           ├── base.html
│           ├── produk_list.html
│           ├── produk_detail.html
│           ├── produk_form.html
│           └── produk_confirm_delete.html
│
├── static/              # File statis (CSS, JS)
│   └── css/
│       └── style.css
│
└── manage.py
```

## Penggunaan
1. **Melihat Daftar Produk**: Akses halaman utama di `/produk/`
2. **Menambah Produk**: Klik tombol "Tambah Produk" dan isi form
3. **Melihat Detail Produk**: Klik tombol "Detail" pada produk yang diinginkan
4. **Edit Produk**: Klik tombol "Edit" pada produk yang ingin diubah
5. **Hapus Produk**: Klik tombol "Hapus" dan konfirmasi penghapusan

## Penjelasan Implementasi

### Model
Model `Produk` memiliki field:
- `nama`: Nama produk
- `deskripsi`: Deskripsi produk
- `harga`: Harga produk
- `stok`: Jumlah stok produk
- `tanggal_input`: Waktu produk ditambahkan

### Views
Sistem menggunakan function-based views untuk operasi CRUD:
- `produk_list`: Menampilkan daftar produk
- `produk_detail`: Menampilkan detail produk
- `produk_create`: Menambah produk baru
- `produk_update`: Mengupdate produk yang ada
- `produk_delete`: Menghapus produk

### Flash Messages
Sistem menggunakan Django messages framework untuk menampilkan notifikasi ketika operasi berhasil dilakukan.

## Tampilan Website
![image](https://github.com/user-attachments/assets/d1627473-af5a-49fd-be56-205bf2ad6e2b)
![image](https://github.com/user-attachments/assets/d5d4250e-df99-4715-9052-387543e54c28)

## Lisensi
[MIT License](LICENSE)

GitHub: [username](https://github.com/WidyaNurulSukma)
