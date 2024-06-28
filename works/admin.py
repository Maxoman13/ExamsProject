from django.contrib import admin

from works.models import Client


# Register your models here.

@admin.register(Client)
class CardAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'surname', 'email', 'first_date', 'update_date', 'services', 'master', 'check_status')

    list_editable = ('master', 'check_status')

    search_fields = ('name', 'surname', 'email', 'services__service_name', 'master__phone', 'check_status__status_name')

    list_filter = ('services', 'master', 'check_status')
