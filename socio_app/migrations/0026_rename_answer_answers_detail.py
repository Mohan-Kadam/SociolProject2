# Generated by Django 4.0.6 on 2022-09-19 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socio_app', '0025_rename_detail_answers_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='answer',
            new_name='detail',
        ),
    ]
