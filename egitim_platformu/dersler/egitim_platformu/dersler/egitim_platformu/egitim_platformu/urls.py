from django.contrib import admin
from django.urls import path
from dersler.views import ders_listesi, konu_detay # Yazdığımız fonksiyonları içeri aktar

urlpatterns = [
    path('admin/', admin.site.urls),  # Yönetim Paneli adresi
    path('', ders_listesi, name='anasayfa'), # www.siteadi.com/ adresi için
    path('konu/<int:konu_id>/', konu_detay, name='konu_detay'), # www.siteadi.com/konu/5/ gibi
]
