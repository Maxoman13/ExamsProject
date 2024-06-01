from django.shortcuts import render
from django.views.generic import TemplateView

info = {
    "menu":
        [{"title": "Главная",
          "url": "/",
          "url_name": "main_page"},
         {"title": "О проекте",
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
