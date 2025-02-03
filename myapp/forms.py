from django import forms
from .models import Cargo

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['jenis_barang', 'berat', 'ukuran', 'agen_pengiriman', 'tujuan_pengiriman', 'nama_pengirim', 'nama_penerima']