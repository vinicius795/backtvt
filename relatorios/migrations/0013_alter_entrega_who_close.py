# Generated by Django 4.0 on 2022-03-26 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('relatorios', '0012_entrega_who_close_alter_entrega_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='who_close',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wclose', to='auth.user'),
        ),
    ]
