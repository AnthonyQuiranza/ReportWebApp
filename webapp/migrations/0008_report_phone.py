# Generated by Django 4.1 on 2022-09-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_report_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='phone',
            field=models.CharField(default='00', max_length=20),
        ),
    ]