# Generated by Django 3.1.4 on 2021-05-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0005_auto_20210510_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrega',
            name='printable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='CTE_FPag',
            field=models.ManyToManyField(blank=True, to='relatorios.CTE_FPag'),
        ),
    ]