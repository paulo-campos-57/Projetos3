# Generated by Django 4.2.6 on 2023-11-26 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0030_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(choices=[('assets/fotos/foto1.png', 'Foto1')], default='assets/fotos/foto1.png', upload_to='fssets/fotos/'),
        ),
    ]
