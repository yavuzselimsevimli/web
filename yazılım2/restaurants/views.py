from django.shortcuts import render, get_object_or_404
from .models import Restaurant

def home(request):
    # Ana sayfa için geçici mesaj
    context = {'mesaj': 'Bu veri views.py dosyasından HTML sayfasına başarıyla ulaştı!'}
    return render(request, 'home.html', context)

def restaurant_list(request):
    # Veritabanındaki tüm restoranları çek
    gercek_restoranlar = Restaurant.objects.all() 
    return render(request, 'restaurant_list.html', {'restoranlar': gercek_restoranlar})

def restaurant_detail(request, id):
    # Sadece tıklanan ID'ye sahip restoranı çek, yoksa 404 hatası ver
    secilen_mekan = get_object_or_404(Restaurant, id=id)
    return render(request, 'restaurant_detail.html', {'mekan': secilen_mekan})

def about(request):
    # Hakkımızda sayfası
    return render(request, 'about.html', {})

def contact(request):
    # İletişim sayfası
    return render(request, 'contact.html', {})