# Generated by Django 4.1.7 on 2023-03-23 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='wishlist',
        ),
    ]