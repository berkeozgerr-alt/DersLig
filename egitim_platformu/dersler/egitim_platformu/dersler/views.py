from django.shortcuts import render, get_object_or_404
from .models import Ders, Konu

# Tüm dersleri ana sayfada listeler
def ders_listesi(request):
    dersler = Ders.objects.all()
    # 'ders_listesi.html' şablonuna veriyi gönderir
    return render(request, 'ders_listesi.html', {'dersler': dersler})

# Seçilen konunun videosunu ve içeriğini gösterir
def konu_detay(request, konu_id):
    # Belirtilen ID'ye sahip konuyu bulur (Bulamazsa 404 hatası verir)
    konu = get_object_or_404(Konu, id=konu_id)
    # 'konu_detay.html' şablonuna konunun verisini gönderir
    return render(request, 'konu_detay.html', {'konu': konu})
