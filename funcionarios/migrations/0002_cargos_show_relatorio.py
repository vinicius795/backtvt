# Generated by Django 3.1.4 on 2021-04-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargos',
            name='SHOW_RELATORIO',
            field=models.BooleanField(default=True),
        ),
    ]
