# Generated by Django 4.0.5 on 2022-08-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='appointment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='report',
            name='appointment_hour',
            field=models.TimeField(),
        ),
    ]