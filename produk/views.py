from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produk
from .forms import ProdukForm

def produk_list(request):
    produk = Produk.objects.all()
    return render(request, 'produk/produk_list.html', {'produk': produk})

def produk_detail(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    return render(request, 'produk/produk_detail.html', {'produk': produk})

def produk_create(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil ditambahkan!")
            return redirect('produk:list')
    else:
        form = ProdukForm()
    return render(request, 'produk/produk_form.html', {'form': form})

def produk_update(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil diupdate!")
            return redirect('produk:list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'produk/produk_form.html', {'form': form})

def produk_delete(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        produk.delete()
        messages.success(request, "Produk berhasil dihapus!")
        return redirect('produk:list')
    return render(request, 'produk/produk_confirm_delete.html', {'produk': produk})