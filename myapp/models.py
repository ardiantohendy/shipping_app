from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cargo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jenis_cargo = models.CharField(max_length=100)
    berat = models.FloatField()
    ukuran = models.FloatField()
    agen_pengiriman = models.CharField(max_length=100)
    tujuan_pengiriman = models.CharField(max_length=100)
    nama_pengirim = models.CharField(max_length=100)
    nama_penerima = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.jenis_cargo} - {self.nama_penerima}'