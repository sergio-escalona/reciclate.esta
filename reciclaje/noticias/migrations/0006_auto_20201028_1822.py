# Generated by Django 3.1.2 on 2020-10-28 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20201028_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='motivo',
            field=models.IntegerField(choices=[[0, 'Sujerencia'], [1, 'Queja'], [2, 'Trabajar con nosotros'], [3, 'Donación']]),
        ),
    ]