# Generated by Django 4.2.6 on 2023-11-13 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0023_rename_datahustorico_userhistorico_datahistorico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistorico',
            name='dataHistorico',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]