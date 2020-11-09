# Generated by Django 3.1.3 on 2020-11-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_product_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.IntegerField(choices=[(1, 'Pièce'), (2, 'kilo (step=0.5)'), (3, 'kilo (step=0.25)')], default=1),
        ),
    ]