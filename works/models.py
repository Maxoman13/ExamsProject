from django.db import models


# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=50, db_column='ClientName')
    surname = models.CharField(max_length=50, db_column='ClientSurname')
    service = models.ForeignKey('ServiceCatalog', on_delete=models.CASCADE, db_column='ServiceNameID')
    price = models.ManyToManyField('ServiceCatalog', through='ServicePrice', related_name='Client',
                                   db_column='ServicePriceID')
    email = models.EmailField(db_column='ClientEmail')
    tg_name = models.CharField(max_length=255, db_column='ClientTg')
    first_date = models.DateTimeField(auto_now=True, db_column='FirstDate')
    update_date = models.DateTimeField(auto_now_add=True, db_column='UpdateDate')
    check_status = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='ClientStatus')

    def __str__(self):
        return f'Клиент {self.name} {self.surname} заказал {self.service}'

    class Meta:
        db_table = 'Service'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceCatalog(models.Model):
    service_name = models.CharField(max_length=50, unique=True, db_column='ServiceName')
    slug_name = models.SlugField(max_length=255, unique=True, db_column='SlugName')

    class Meta:
        db_table = 'ServiceCatalog'
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Вид услуг'

    def __str__(self):
        return f'Услуга {self.service_name}'


class ServicePrice(models.Model):
    service_name = models.ForeignKey(ServiceCatalog, on_delete=models.CASCADE, db_column='ServiceNameID')
    service_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, db_column='ServicePrice')
    service_client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='ClientID')

    class Meta:
        db_table = 'ServicePrice'
        verbose_name = 'Цена услуги'
        verbose_name_plural = 'Цены услуг'

    def __str__(self):
        return f'Цена услуги {self.service_name} для {self.service_client}'


class Status(models.Model):
    status_name = models.CharField(max_length=255, db_column='StatusName')

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус услуги'
        verbose_name_plural = 'Статус услуг'

    def __str__(self):
        return f'Статус {self.status_name}'
