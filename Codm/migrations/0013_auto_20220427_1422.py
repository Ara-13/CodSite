# Generated by Django 3.2.5 on 2022-04-27 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codm', '0012_auto_20220422_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codaccount',
            name='region',
            field=models.CharField(choices=[('220', 'Iran'), ('360', 'India'), ('560', 'Europe')], default='IR', max_length=3, verbose_name='ریجن'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('w4c', 'ثبت شده'), ('dn', 'تکمیل شده'), ('cl', 'لغو شده'), ('w4ti', 'در انتظار اصلاح اطلاعات')], default='w4c', max_length=5),
        ),
    ]