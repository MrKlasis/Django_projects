# Generated by Django 4.2.6 on 2023-10-24 15:31

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_begin',
            field=models.DateField(default=django.utils.datetime_safe.date.today, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_chang',
            field=models.DateField(default=django.utils.datetime_safe.date.today, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Изображение'),
        ),
    ]
