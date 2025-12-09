from django.db import models

# Ders Kategorisi (Örn: Matematik, Fen)
class Ders(models.Model):
    isim = models.CharField(max_length=200)
    aciklama = models.TextField()
    
    # Kullanımı kolay olması için isim ile çağrılmasını sağlar
    def __str__(self):
        return self.isim

# Dersin İçindeki Konular/Videolar
class Konu(models.Model):
    # Bu satır, bu konunun hangi derse ait olduğunu belirtir
    ders = models.ForeignKey(Ders, on_delete=models.CASCADE, related_name='konular')
    baslik = models.CharField(max_length=200)
    video_linki = models.URLField(help_text="Örn: https://www.youtube.com/watch?v=video_ID")
    icerik_metni = models.TextField()
    sira_numarasi = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.ders.isim}: {self.baslik}"
