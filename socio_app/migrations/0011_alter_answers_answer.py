# Generated by Django 4.0.6 on 2022-09-19 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socio_app', '0010_answers_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socio_app.queries'),
        ),
    ]
