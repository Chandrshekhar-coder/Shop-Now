# Generated by Django 3.1.5 on 2021-04-15 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20210415_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delevery_time',
            field=models.CharField(default='', max_length=500),
        ),
    ]
