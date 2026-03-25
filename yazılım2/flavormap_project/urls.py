from django.contrib import admin
from django.urls import path
from restaurants import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('restoranlar/', views.restaurant_list, name='restaurant_list'),
    path('restoran/<int:id>/', views.restaurant_detail, name='restaurant_detail'),
    path('hakkinda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
]