# Generated by Django 2.1.5 on 2019-02-15 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('categoria', models.CharField(max_length=30)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('marca', models.CharField(max_length=30)),
            ],
        ),
    ]
