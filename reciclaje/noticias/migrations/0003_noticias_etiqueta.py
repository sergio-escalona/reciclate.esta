# Generated by Django 3.1.2 on 2020-10-26 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20201026_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='etiqueta',
            field=models.TextField(default='publico'),
        ),
    ]