# Generated by Django 4.0.5 on 2022-08-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('passport', models.CharField(max_length=10)),
                ('folio', models.CharField(max_length=20)),
                ('appointment_date', models.DateField(auto_now=True)),
                ('appointment_hour', models.DateTimeField()),
                ('is_authorized', models.BooleanField()),
            ],
        ),
    ]
