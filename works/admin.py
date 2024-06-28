from django.contrib import admin

from works.models import Client, Master


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'surname', 'email', 'first_date', 'update_date', 'services', 'master', 'check_status')

    list_editable = ('master', 'check_status')

    search_fields = ('name', 'surname', 'email', 'services__service_name', 'master__phone', 'check_status__status_name')

    list_filter = ('services', 'master', 'check_status')


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone')

    list_editable = ('first_name', 'last_name', 'phone')
