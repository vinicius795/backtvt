# Generated by Django 3.1.4 on 2021-04-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cte',
            name='NR_CONTROLE',
            field=models.CharField(max_length=12),
        ),
    ]