# Generated by Django 3.1.5 on 2021-03-06 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0005_auto_20210305_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='order',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='product',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='user_profile',
        ),
    ]
