# Generated by Django 3.1.7 on 2022-03-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0006_remove_customer_display_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='blacklisted',
            field=models.CharField(choices=[('yes', 'yes '), ('no', 'no')], default='no', max_length=50),
        ),
    ]
