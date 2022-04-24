# Generated by Django 3.2.5 on 2022-04-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='background',
            field=models.ImageField(max_length=5000, null=True, upload_to='Products/media/Products/product-backgrounds/'),
        ),
        migrations.AddField(
            model_name='group',
            name='logo',
            field=models.ImageField(max_length=5000, null=True, upload_to='Products/media/Products/product-logos/'),
        ),
    ]
