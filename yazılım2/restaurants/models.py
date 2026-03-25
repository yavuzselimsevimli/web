from django.db import models

# Kategori Tablosu (Örn: İtalyan, Türk Mutfağı, Fast Food)
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategori Adı")

    def __str__(self):
        return self.name  # Sitede "Category object 1" yerine adıyla görünmesini sağlar

# Restoran Tablosu
class Restaurant(models.Model):
    # Fiyat aralığı seçenekleri (Dropdown menü için)
    PRICE_CHOICES = [
        ('€', 'Ucuz'),
        ('€€', 'Orta'),
        ('€€€', 'Pahalı'),
    ]

    name = models.CharField(max_length=100, verbose_name="Restoran Adı")
    description = models.TextField(verbose_name="Açıklama")
    address = models.CharField(max_length=250, verbose_name="Adres")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    price_range = models.CharField(max_length=5, choices=PRICE_CHOICES, verbose_name="Fiyat Aralığı")
    
    # Kategori ile Restoranı bağlıyoruz (Bir restoranın bir kategorisi olur)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategori")

    def __str__(self):
        return self.name