# Generated by Django 3.1.4 on 2021-05-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorios', '0006_auto_20210510_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='CTENotFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cte', models.CharField(max_length=44, unique=True)),
                ('relatorio', models.ManyToManyField(to='relatorios.ENTREGA')),
            ],
        ),
    ]