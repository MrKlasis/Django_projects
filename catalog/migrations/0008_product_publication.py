# Generated by Django 4.2.6 on 2023-11-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publication',
            field=models.BooleanField(default=False, verbose_name='публикация'),
        ),
    ]
