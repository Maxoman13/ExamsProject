from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class MainPage(TemplateView):
    template_name = 'main_page.html'


class AboutPage(TemplateView):
    template_name = 'about.html'


class ContacsPage(TemplateView):
    template_name = 'contacts.html'