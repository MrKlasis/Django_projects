# Generated by Django 4.2.6 on 2023-11-03 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verify',
            field=models.BooleanField(default=False, verbose_name='верификация почты'),
        ),
    ]
