# Generated by Django 4.2.6 on 2023-11-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_email_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='token', max_length=100, verbose_name='token'),
        ),
    ]
