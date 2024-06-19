from django.db import models


# Create your models here.


class Master(models.Model):
    first_name = models.CharField(max_length=50, db_column='MasterFirstName')
    last_name = models.CharField(max_length=50, db_column='MasterLastName')
    phone = models.CharField(max_length=15, db_column='MasterPhone')
    services = models.ManyToManyField('ServiceCatalog', related_name='masters')

    class Meta:
        db_table = 'Master'
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ServiceCatalog(models.Model):
    service_image = models.ImageField(db_column='ServiceImage')
    service_name = models.CharField(max_length=50, unique=True, db_column='ServiceName')
    price = models.DecimalField(max_digits=7, decimal_places=2, db_column='ServicePrice')
    service_description = models.TextField(max_length=1000, db_column='ServiceDescription')
    slug_name = models.SlugField(max_length=255, unique=True, db_column='SlugName')

    class Meta:
        db_table = 'ServiceCatalog'
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Вид услуг'

    def __str__(self):
        return f'Услуга {self.service_name} - {self.price} руб.'


class Client(models.Model):
    name = models.CharField(max_length=50, db_column='ClientName')
    surname = models.CharField(max_length=50, db_column='ClientSurname')
    email = models.EmailField(db_column='ClientEmail')
    first_date = models.DateTimeField(auto_now=True, db_column='FirstDate')
    update_date = models.DateTimeField(auto_now_add=True, db_column='UpdateDate')
    services = models.ManyToManyField('ServiceCatalog', related_name='clients')
    master = models.ForeignKey(Master, on_delete=models.CASCADE, db_column='MasterID')
    check_status = models.ForeignKey('Status', on_delete=models.CASCADE, db_column='StatusID')

    class Meta:
        db_table = 'Client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'Клиент {self.name} {self.surname} заказал услуги у {self.master}'


class Status(models.Model):
    status_name = models.CharField(max_length=255, db_column='StatusName')

    class Meta:
        db_table = 'Status'
        verbose_name = 'Статус услуги'
        verbose_name_plural = 'Статус услуг'

    def __str__(self):
        return f'Статус {self.status_name}'
