# Generated by Django 5.0.7 on 2024-08-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_image_url_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevent',
            name='end_time',
        ),
        migrations.AddField(
            model_name='product',
            name='duration',
            field=models.CharField(default='90 minutes', max_length=50),
        ),
    ]
