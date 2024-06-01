from django.db import models

# Create your models here.

SERVICE_TYPE = {}


class Client(models.Model):
    id = models.AutoField(primary_key=True, db_column='ClientID')
    name = models.CharField(max_length=50, db_column='ClientName')
    surname = models.CharField(max_length=50, db_column='ClientSurname')
    service = models.ForeignKey('ServiceCatalog', on_delete=models.CASCADE, db_column='ClientService')
    price = models.ManyToManyField('ServicePrice', though='ServiceCatalog', on_delete=models.CASCADE)
    email = models.EmailField(db_column='ClientEmail')
    tg_name = models.CharField(max_length=50, db_column='ClientTg')
    first_date = models.DateTimeField(db_column='FirstDate')
    update_date = models.DateTimeField(db_column='UpdateDate')
    check_status = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='ClientStatus')

    def __str__(self):
        return f'Клиент {self.name} - {self.surname} заказал {self.service}'

    class Meta:
        db_table = 'Service'  # имя таблицы в базе данных
        verbose_name = 'Услуга'  # имя модели в единственном числе
        verbose_name_plural = 'Услуги'  # имя модели во множественном числе


class ServiceCatalog(models.Model):
    id = models.AutoField(primary_key=True, db_column='ServiceID')
    service_name = models.CharField(max_length=50, db_column='ServiceName')

    class Meta:
        db_table = 'ServiceCatalog'
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Вид услуг'

    def __str__(self):
        return f'Услуга {self.service_name}'


class ServicePrice(models.Model):
    id = models.AutoField(primary_key=True, db_column='ServicePriceID')
    service_name = models.ForeignKey('ServiceCatalog', on_delete=models.CASCADE, db_column='ServiceName')
    service_price = models.DecimalField(max_length=7, db_column='ServicePrice')

    class Meta:
        db_table = 'ServiceCatalog'
        verbose_name = 'Цена услуги'
        verbose_name_plural = 'Цены услуг'

    def __str__(self):
        return f'Цена услуги {self.service_name}'


class Status(models.Model):
    id = models.AutoField(primary_key=True, db_column='StatusPriceID')
    status_name = models.CharField(max_length=50, db_column='StatusName')

    def __str__(self):
        return f'Статус {self.status_name}'
