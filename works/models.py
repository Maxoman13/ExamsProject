from django.db import models
from django.urls import reverse


# Create your models here.


class Master(models.Model):
    first_name = models.CharField(max_length=50, db_column='MasterFirstName')
    last_name = models.CharField(max_length=50, db_column='MasterLastName')
    phone = models.CharField(max_length=15, db_column='MasterPhone')

    class Meta:
        db_table = 'Master'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Status(models.Model):
    status_name = models.CharField(max_length=255, db_column='StatusName')

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус услуги'
        verbose_name_plural = 'Статус услуг'

    def __str__(self):
        return f'{self.status_name}'


class ServiceCatalog(models.Model):
    service_image = models.ImageField(upload_to="photos/", default=None, blank=True,
                                      null=True, db_column='ServiceImage')
    service_name = models.CharField(max_length=50, unique=True, db_column='ServiceName')
    price = models.DecimalField(max_digits=7, decimal_places=2, db_column='ServicePrice')
    service_description = models.TextField(max_length=1000, db_column='ServiceDescription')
    slug_name = models.SlugField(max_length=255, unique=True, db_column='SlugName')

    class Meta:
        db_table = 'ServiceCatalog'
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Вид услуг'

    def __str__(self):
        return f'{self.service_name} - {self.price}'

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug_name})


class Client(models.Model):
    name = models.CharField(max_length=50, db_column='ClientName')
    surname = models.CharField(max_length=50, db_column='ClientSurname')
    email = models.EmailField(db_column='ClientEmail')
    first_date = models.DateTimeField(auto_now=True, db_column='FirstDate')
    update_date = models.DateTimeField(auto_now_add=True, db_column='UpdateDate')
    services = models.ForeignKey(ServiceCatalog, on_delete=models.CASCADE, db_column='ClientService')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, blank=True, null=True, db_column='MasterID')
    check_status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True, db_column='StatusID')

    class Meta:
        db_table = 'Client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Клиент {self.name} {self.surname} заказал услуги у {self.master}'
