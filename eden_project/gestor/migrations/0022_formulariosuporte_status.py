# Generated by Django 4.2.6 on 2023-11-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0021_midia_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulariosuporte',
            name='status',
            field=models.BooleanField(default='False'),
        ),
    ]