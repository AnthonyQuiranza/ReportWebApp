# Generated by Django 4.1 on 2022-09-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_report_pdf_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='password',
            field=models.CharField(default='12345678', max_length=40),
        ),
    ]