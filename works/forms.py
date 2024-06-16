from django import forms
from .models import Client, ServiceCatalog
from django.core.exceptions import ValidationError
import re


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'email', 'master', 'services']
        widgets = {
            'master': forms.Select(attrs={'onchange': 'loadServices()'}),
            'services': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['services'].queryset = ServiceCatalog.objects.none()

        if 'master' in self.data:
            try:
                master_id = int(self.data.get('master'))
                self.fields['services'].queryset = ServiceCatalog.objects.filter(masters__id=master_id).order_by('service_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['services'].queryset = self.instance.master.services.order_by('service_name')

    def save(self, *args, **kwargs):
        instance = super().save(commit=False)
        instance.save()

        return instance
