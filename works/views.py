from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from works.forms import ClientForm
from works.models import Client, ServiceCatalog

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


class CatalogPage(MenuMixin, ListView):
    model = ServiceCatalog
    template_name = 'catalog.html'
    context_object_name = 'services'


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


class Thanks(MenuMixin, TemplateView):
    template_name = 'thanks.html'


class ShowService(MenuMixin, DetailView):
    model = ServiceCatalog
    template_name = 'service_detail.html'
    slug_url_kwarg = 'service_slug'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['service']
        return context

    def get_object(self):
        return get_object_or_404(ServiceCatalog, slug_name=self.kwargs[self.slug_url_kwarg])


def page_not_found(request, exception, template_name='404.html'):
    response = render(request, template_name)
    response.status_code = 404
    return response
