from django.db import models


class Talep(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField(blank=True)
    olusturma = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-olusturma"]

    def sozluk(self):
        return {
            "id": self.id,
            "baslik": self.baslik,
            "aciklama": self.aciklama,
            "olusturma": self.olusturma.isoformat(),
        }
