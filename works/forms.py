from django import forms
from .models import Client, ServiceCatalog, Status
from django.core.exceptions import ValidationError
import re


class ClientForm(forms.ModelForm):
    services = forms.ModelChoiceField(queryset=ServiceCatalog.objects.all(), empty_label="Услуга не выбрана",
                                      label='Услуга', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'services']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'email': 'Электронная почта',
            'services': 'Услуга'}

    def save(self, *args, **kwargs):
        instance = super().save(commit=False)
        instance.save()

        return instance
