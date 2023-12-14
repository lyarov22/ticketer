from django import forms
from .models import Bench

class BenchForm(forms.ModelForm):
    class Meta:
        model = Bench
        fields = ['avatar', 'deskription', 'type', 'district', 'created_date']