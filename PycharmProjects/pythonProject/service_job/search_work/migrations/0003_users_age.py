# Generated by Django 3.1.5 on 2021-01-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_work', '0002_auto_20210112_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=11, verbose_name='Возраст пользователя'),
            preserve_default=False,
        ),
    ]
