# Generated by Django 3.1.5 on 2021-01-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date_register',
            field=models.DateField(verbose_name='Дата регистрации'),
        ),
    ]