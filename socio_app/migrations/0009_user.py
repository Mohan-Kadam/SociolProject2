# Generated by Django 4.0.6 on 2022-09-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio_app', '0008_queries_approval'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
            ],
        ),
    ]
