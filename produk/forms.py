from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama', 'deskripsi', 'harga', 'stok']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control'}),
        }