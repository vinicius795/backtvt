# Generated by Django 4.0 on 2022-01-06 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0008_ctenotfound_f_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrega',
            name='date_closed',
            field=models.DateTimeField(blank=True, default=datetime.date(2022, 1, 6)),
        ),
    ]
