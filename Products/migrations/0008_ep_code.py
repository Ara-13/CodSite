# Generated by Django 3.2.5 on 2022-04-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_auto_20220422_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='ep',
            name='code',
            field=models.IntegerField(null=True),
        ),
    ]
