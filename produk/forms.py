from django import forms 
from .models import Produk  

class ProdukForm(forms.ModelForm):  # Mendefinisikan kelas ProdukForm yang mewarisi dari forms.ModelForm
    class Meta:  # Kelas Meta untuk konfigurasi form
        model = Produk  # Menentukan model yang digunakan adalah Produk
        fields = ['nama', 'deskripsi', 'harga', 'stok']  # Menentukan field yang akan ditampilkan di form

        widgets = {  # Menentukan widget kustom untuk masing-masing field agar tampilan form lebih baik
            'nama': forms.TextInput(attrs={'class': 'form-control'}),  # Menggunakan widget TextInput dengan class CSS 'form-control' untuk field 'nama'
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),  # Menggunakan widget Textarea dengan class CSS 'form-control' untuk field 'deskripsi'
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),  # Menggunakan widget NumberInput dengan class CSS 'form-control' untuk field 'harga'
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),  # Menggunakan widget NumberInput dengan class CSS 'form-control' untuk field 'stok'
        }
