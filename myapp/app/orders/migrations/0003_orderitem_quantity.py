# Generated by Django 4.2 on 2023-04-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
