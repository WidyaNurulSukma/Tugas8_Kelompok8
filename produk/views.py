from django.shortcuts import render  # Untuk merender template HTML

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404  # Fungsi bantu untuk view
from django.contrib import messages  # Untuk menampilkan pesan notifikasi
from .models import Produk  # Mengimpor model Produk
from .forms import ProdukForm  # Mengimpor form ProdukForm

def produk_list(request):  # Menampilkan semua produk
    produk = Produk.objects.all()  # Mengambil semua data produk
    return render(request, 'produk/produk_list.html', {'produk': produk})  # Menampilkan template dengan data produk

def produk_detail(request, pk):  # Menampilkan detail satu produk
    produk = get_object_or_404(Produk, pk=pk)  # Mengambil produk berdasarkan primary key atau 404 jika tidak ada
    return render(request, 'produk/produk_detail.html', {'produk': produk})  # Menampilkan template detail produk

def produk_create(request):  # Menambahkan produk baru
    if request.method == 'POST':  # Jika form dikirim
        form = ProdukForm(request.POST)  # Buat form dengan data POST
        if form.is_valid():  # Validasi form
            form.save()  # Simpan data produk
            messages.success(request, "Produk berhasil ditambahkan!")  # Tampilkan pesan sukses
            return redirect('produk:list')  # Redirect ke daftar produk
    else:
        form = ProdukForm()  # Form kosong untuk GET request
    return render(request, 'produk/produk_form.html', {'form': form})  # Tampilkan form

def produk_update(request, pk):  # Mengedit data produk
    produk = get_object_or_404(Produk, pk=pk)  # Ambil produk atau 404
    if request.method == 'POST':  # Jika form dikirim
        form = ProdukForm(request.POST, instance=produk)  # Buat form dengan data dan instance produk
        if form.is_valid():  # Validasi form
            form.save()  # Simpan perubahan
            messages.success(request, "Produk berhasil diupdate!")  # Pesan sukses
            return redirect('produk:list')  # Redirect ke daftar produk
    else:
        form = ProdukForm(instance=produk)  # Form dengan data produk untuk diedit
    return render(request, 'produk/produk_form.html', {'form': form})  # Tampilkan form

def produk_delete(request, pk):  # Menghapus produk
    produk = get_object_or_404(Produk, pk=pk)  # Ambil produk atau 404
    if request.method == 'POST':  # Jika form konfirmasi dikirim
        produk.delete()  # Hapus produk
        messages.success(request, "Produk berhasil dihapus!")  # Pesan sukses
        return redirect('produk:list')  # Redirect ke daftar produk
    return render(request, 'produk/produk_confirm_delete.html', {'produk': produk})  # Tampilkan konfirmasi hapus
