# Generated by Django 4.0.6 on 2022-09-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio_app', '0028_addservice_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addservice',
            name='detail',
            field=models.TextField(default='', max_length=200),
        ),
    ]
