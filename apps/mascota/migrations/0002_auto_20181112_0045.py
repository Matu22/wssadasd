# Generated by Django 2.1.2 on 2018-11-12 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(choices=[('DISPONIBLE', 'Disponible'), ('NO DISPONIBLE', 'No Disponible')], max_length=15),
        ),
    ]