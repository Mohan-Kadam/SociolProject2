# Generated by Django 4.0.6 on 2022-09-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio_app', '0007_queries_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='queries',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
