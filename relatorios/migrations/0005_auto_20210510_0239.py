# Generated by Django 3.1.4 on 2021-05-10 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0004_auto_20210510_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='CTE_FPag',
            field=models.ManyToManyField(null=True, to='relatorios.CTE_FPag'),
        ),
    ]