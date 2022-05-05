# Generated by Django 3.1.7 on 2022-02-26 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_customer_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='photo',
            new_name='display_photo',
        ),
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='bank',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='card_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='occupation',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
