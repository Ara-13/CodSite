# Generated by Django 3.2.5 on 2022-03-27 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('pub_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('available', 'موجود'), ('sold', 'فروخته شد'), ('w4p', 'در انتظار تایید')], default='w4p', max_length=10)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, max_length=300, null=True)),
                ('show', models.BooleanField(default=True)),
                ('Type', models.CharField(choices=[('bigbanner', 'بنر بزرگ'), ('middlebanner', 'بنر متوسط'), ('smallbanner', 'بنر کوچک')], default='smallbanner', max_length=12)),
                ('picture', models.ImageField(upload_to='Codm/static/assets/img/banner')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsiveSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, max_length=300, null=True)),
                ('show', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to='Codm/static/assets/img/main-slider/slider-responsive')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.URLField(blank=True, max_length=300, null=True)),
                ('show', models.BooleanField(default=True)),
                ('picture', models.ImageField(upload_to='Codm/static/assets/img/main-slider')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='Codm/media/account_pictures/<django.db.models.query_utils.DeferredAttribute object at 0x000001C423281D60>')),
                ('url', models.URLField()),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Codm.account')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_number', models.IntegerField(primary_key=True, serialize=False)),
                ('factor_number', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('final_price', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('w4c', 'در انتظار بررسی'), ('dn', 'تکمیل شده'), ('cl', 'لغو شده'), ('w4ti', 'در انتظار اصلاح اطلاعات')], default='w4c', max_length=5)),
                ('product', models.ManyToManyField(to='Products.Product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-order_number'],
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('activision', 'اکتیویژن'), ('facebook', 'فیسبوک'), ('gmail', 'جیمیل'), ('apple_id', 'اپل آی-دی'), ('line', 'لاین')], default='Activision', max_length=10)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Codm.account')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Codm/media/account_pictures/<django.db.models.query_utils.DeferredAttribute object at 0x000001C423281D60>')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Codm.account')),
            ],
        ),
        migrations.CreateModel(
            name='CodAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Codm/media/account_pictures/<django.db.models.query_utils.DeferredAttribute object at 0x000001C423281D60>')),
                ('region', models.CharField(choices=[('220', 'Iran'), ('360', 'India'), ('560', 'Europe')], default='IR', max_length=3)),
                ('cp', models.IntegerField(blank=True, default=0, null=True)),
                ('c', models.IntegerField(blank=True, default=0, null=True)),
                ('multi_ranked', models.CharField(blank=True, max_length=200, null=True)),
                ('battle_ranked', models.CharField(blank=True, max_length=200, null=True)),
                ('battle_pass', models.TextField(blank=True, max_length=900, null=True)),
                ('description', models.TextField(blank=True, max_length=900, null=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Codm.account')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('nf', 'NotFinished'), ('f', 'Finished')], default='nf', max_length=2)),
                ('final_price', models.IntegerField(blank=True, default=0, null=True)),
                ('account', models.ManyToManyField(blank=True, to='Codm.Account')),
                ('product', models.ManyToManyField(blank=True, to='Products.Product')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Codm.order'),
        ),
        migrations.AddField(
            model_name='account',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
