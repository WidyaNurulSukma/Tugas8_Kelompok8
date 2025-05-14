from django.urls import path
from . import views

app_name = 'produk'

urlpatterns = [
    path('', views.produk_list, name='list'),
    path('detail/<int:pk>/', views.produk_detail, name='detail'),
    path('tambah/', views.produk_create, name='create'),
    path('edit/<int:pk>/', views.produk_update, name='update'),
    path('hapus/<int:pk>/', views.produk_delete, name='delete'),
]