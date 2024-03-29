# Generated by Django 3.2.5 on 2022-03-27 13:34

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=300, null=True, unique=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('sells', models.IntegerField(default=0, null=True)),
                ('buys', models.IntegerField(default=0, null=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('user_type', models.CharField(choices=[('superadmin', 'SuperAdmin'), ('admin', 'Admin'), ('user', 'User')], default='user', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
