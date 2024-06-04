from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from works.forms import ClientForm
from works.models import Client

info = {
    "menu":
        [{"title": "Главная",
          "url": "/",
          "url_name": "main_page"},
         {"title": "О нас",
          "url": "/about/",
          "url_name": "about"},
         {"title": "Услуги и цены",
          "url": "/catalog/",
          "url_name": "catalog"},
         {"title": "Контакты",
          "url": "/contacts/",
          "url_name": "contacts"},
         ]}


class MenuMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(info)
        return context


# Create your views here.
class MainPage(MenuMixin, TemplateView):
    template_name = 'main_page.html'


class AboutPage(MenuMixin, TemplateView):
    template_name = 'about.html'


class ContactsPage(MenuMixin, TemplateView):
    template_name = 'contacts.html'


class CatalogPage(MenuMixin, TemplateView):
    template_name = 'catalog.html'


class AddServiceCreateView(MenuMixin, CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'add_service.html'
    success_url = reverse_lazy('thanks')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = info['menu']
        return context


class Thanks(TemplateView):
    template_name = 'thanks.html'
