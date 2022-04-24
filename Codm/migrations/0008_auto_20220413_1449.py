# Generated by Django 3.2.5 on 2022-04-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Codm', '0007_auto_20220327_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='picture',
            field=models.ImageField(blank=True, max_length=300, null=True, upload_to='account_pictures/<django.db.models.fields.IntegerField>/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=300, upload_to='account_pictures/<django.db.models.fields.related.ForeignKey>/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(max_length=500, null=True, upload_to='account_videos/<django.db.models.fields.related.OneToOneField>/'),
        ),
    ]