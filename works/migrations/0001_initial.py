# Generated by Django 4.2 on 2024-06-25 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='MasterFirstName', max_length=50)),
                ('last_name', models.CharField(db_column='MasterLastName', max_length=50)),
                ('phone', models.CharField(db_column='MasterPhone', max_length=15)),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
                'db_table': 'Master',
            },
        ),
        migrations.CreateModel(
            name='ServiceCatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_image', models.ImageField(blank=True, db_column='ServiceImage', default=None, null=True, upload_to='photos/')),
                ('service_name', models.CharField(db_column='ServiceName', max_length=50, unique=True)),
                ('price', models.DecimalField(db_column='ServicePrice', decimal_places=2, max_digits=7)),
                ('service_description', models.TextField(db_column='ServiceDescription', max_length=1000)),
                ('slug_name', models.SlugField(db_column='SlugName', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Вид услуги',
                'verbose_name_plural': 'Вид услуг',
                'db_table': 'ServiceCatalog',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(db_column='StatusName', max_length=255)),
            ],
            options={
                'verbose_name': 'Статус услуги',
                'verbose_name_plural': 'Статус услуг',
                'db_table': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='ClientName', max_length=50)),
                ('surname', models.CharField(db_column='ClientSurname', max_length=50)),
                ('email', models.EmailField(db_column='ClientEmail', max_length=254)),
                ('first_date', models.DateTimeField(auto_now=True, db_column='FirstDate')),
                ('update_date', models.DateTimeField(auto_now_add=True, db_column='UpdateDate')),
                ('check_status', models.ForeignKey(blank=True, db_column='StatusID', null=True, on_delete=django.db.models.deletion.CASCADE, to='works.status')),
                ('master', models.ForeignKey(blank=True, db_column='MasterID', null=True, on_delete=django.db.models.deletion.CASCADE, to='works.master')),
                ('services', models.ForeignKey(db_column='ClientService', on_delete=django.db.models.deletion.CASCADE, to='works.servicecatalog')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'db_table': 'Client',
            },
        ),
    ]
