# Generated by Django 3.2.5 on 2022-02-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Codm', '0008_auto_20220210_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codaccount',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Codm.cart'),
        ),
    ]
