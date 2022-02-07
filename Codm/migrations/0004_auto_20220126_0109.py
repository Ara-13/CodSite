# Generated by Django 3.2.5 on 2022-01-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codm', '0003_auto_20220126_0107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codaccount',
            old_name='user',
            new_name='seller',
        ),
        migrations.AlterField(
            model_name='codaccount',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/account_pictures'),
        ),
    ]
