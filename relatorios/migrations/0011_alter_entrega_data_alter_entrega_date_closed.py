# Generated by Django 4.0 on 2022-01-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0010_alter_entrega_date_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='DATA',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='date_closed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
