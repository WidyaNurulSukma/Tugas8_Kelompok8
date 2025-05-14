from django.db import models  # Mengimpor modul models dari Django untuk membuat model basis data
from django.urls import reverse  # Mengimpor fungsi reverse untuk mendapatkan URL berdasarkan nama rute

class Produk(models.Model):  # Mendefinisikan model Produk yang mewarisi dari models.Model
    nama = models.CharField(max_length=100)  # Kolom nama sebagai karakter dengan panjang maksimal 100
    deskripsi = models.TextField()  # Kolom deskripsi sebagai teks bebas tanpa batas panjang khusus
    harga = models.DecimalField(max_digits=10, decimal_places=2)  # Kolom harga bertipe desimal dengan maksimal 10 digit dan 2 angka di belakang koma
    stok = models.IntegerField()  # Kolom stok sebagai bilangan bulat
    tanggal_input = models.DateTimeField(auto_now_add=True)  # Kolom tanggal_input yang otomatis diisi dengan waktu saat objek dibuat

    def __str__(self):  # Metode spesial untuk representasi string dari objek Produk
        return self.nama  # Mengembalikan nama produk sebagai representasi string

    def get_absolute_url(self):  # Metode untuk mendapatkan URL detail dari produk ini
        return reverse('produk:detail', kwargs={'pk': self.pk})  # Mengembalikan URL berdasarkan nama rute 'produk:detail' dengan parameter pk (primary key) dari produk
