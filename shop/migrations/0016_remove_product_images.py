# Generated by Django 3.1.5 on 2021-04-13 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
    ]
