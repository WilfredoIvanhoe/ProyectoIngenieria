# Generated by Django 3.0.3 on 2020-03-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavado', '0003_auto_20200306_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugarcompra',
            name='direccion',
            field=models.CharField(max_length=100),
        ),
    ]
