# Generated by Django 3.2.5 on 2022-04-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codm', '0008_auto_20220413_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='picture',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='account_pictures/'),
        ),
    ]
