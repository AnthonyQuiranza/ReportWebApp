# Generated by Django 4.1 on 2022-08-28 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_report_verification_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='pdf_url',
            field=models.URLField(default='https://citascuba.reprogramacion-gob.mx/'),
        ),
    ]
