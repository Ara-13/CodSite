# Generated by Django 3.2.5 on 2022-04-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codm', '0009_alter_account_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='group',
            field=models.CharField(choices=[('codm', 'کالاف دیوتی موبایل'), ('coc', 'کلش آف کلنز'), ('pubg', 'پابجی')], default='codm', max_length=10),
        ),
    ]