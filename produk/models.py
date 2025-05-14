from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    tanggal_input = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nama
    
    def get_absolute_url(self):
        return reverse('produk:detail', kwargs={'pk': self.pk})