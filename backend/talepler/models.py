from django.db import models


class Talep(models.Model):
    ONCELIKLER = [("Düşük", "Düşük"), ("Normal", "Normal"), ("Yüksek", "Yüksek")]

    baslik = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True)
    oncelik = models.CharField(max_length=10, choices=ONCELIKLER, default="Normal")
    olusturma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-olusturma"]

    def sozluk(self):
        return {
            "id": self.id,
            "baslik": self.baslik,
            "aciklama": self.aciklama,
            "oncelik": self.oncelik,
            "olusturma": self.olusturma.isoformat(),
        }
