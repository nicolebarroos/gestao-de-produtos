# Generated by Django 2.1.5 on 2019-04-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0002_itemdopedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='nfe_emitida',
            field=models.BooleanField(default=False),
        ),
    ]