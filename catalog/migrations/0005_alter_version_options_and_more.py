# Generated by Django 4.2.6 on 2023-10-30 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='version',
            options={'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.RenameField(
            model_name='version',
            old_name='version_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='version',
            old_name='version_number',
            new_name='number',
        ),
    ]