from django.db import models
from django.forms import DateField
#important
#from django.conf import settings
#User = settings.AUTH_USER_MODEL
from Users.models import User
from Products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_number = models.IntegerField(primary_key=True)
    factor_number = models.IntegerField()
    product = models.ManyToManyField(Product, blank=True)
    date = models.DateField(auto_now=True)

    Status = (
        ('w4c', 'ثبت شده'),
        ('dn', 'تکمیل شده'),
        ('cl', 'لغو شده'),
        ('w4ti', 'در انتظار اصلاح اطلاعات'),
    )
    final_price = models.IntegerField(null=True)

    status = models.CharField(max_length=5, choices=Status, default='w4c')
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return 'user:{}; order:{}; factor{}'.format(self.user, self.order_number, self.factor_number)

class Account(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    code = models.IntegerField(primary_key=True)

    picture = models.ImageField(upload_to='account_pictures/', max_length=300, blank=True, null=True)

    pub_date = models.DateField(null=True)

    Status = (
        ('available', 'موجود'),
        ('sold', 'فروخته شد'),
        ('w4p', 'در انتظار تایید'),
        ('canceled', 'لغو شده'),
    )

    Group = (
        ('codm', 'کالاف دیوتی موبایل'),
        ('coc', 'کلش آف کلنز'),
        ('pubg', 'پابجی')
    )
    group = models.CharField(max_length=10, choices=Group, default='codm')
    status = models.CharField(max_length=10, choices=Status, default='w4p')

    price = models.IntegerField()
    
    def __str__(self):
        return '{}---{}---{}---{}T'.format(self.seller, self.code, self.status, self.price)

class CodAccount(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    Region = (
        ('220', 'Iran'),
        ('360', 'India'),
        ('560', 'Europe'),
    )

    region = models.CharField(max_length=3, choices=Region, default='IR')

    cp = models.IntegerField(default=0, blank=True, null=True)
    c = models.IntegerField(default=0, blank=True, null=True)

    multi_ranked = models.CharField(max_length=200, blank=True, null=True)
    battle_ranked = models.CharField(max_length=200, blank=True, null=True)

    battle_pass = models.TextField(max_length=900, blank=True, null=True)
    description = models.TextField(max_length=900, blank=True, null=True)

    def __str__(self):
        return 'CodAccount:{}'.format(self.account.code)


class Image(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account_pictures/', max_length=300)
    
    def __str__(self):
        return 'Account:{}'.format(self.account)

class Video(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    video = models.FileField(upload_to='account_videos/', max_length=500, null=True)
    url = models.URLField(blank=True, null=True)

class Link(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    Ts = (
        ('activision' , 'اکتیویژن'),
        ('facebook' , 'فیسبوک'),
        ('gmail' , 'جیمیل'),
        ('apple_id' , 'اپل آی-دی'),
        ('line' , 'لاین'),
    )
    Type = models.CharField(max_length=10, choices=Ts, default="Activision")
    mail = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{}-account--{}'.format(self.Type, self.account.code)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    account = models.ManyToManyField(Account, blank=True)
    product = models.ManyToManyField(Product, blank=True)
    S = (
        ('nf', 'NotFinished'),
        ('f', 'Finished')
    )
    status = models.CharField(max_length=2, choices=S, default='nf')
    final_price = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return 'Cart({0})'.format(self.user)

class Slider(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='Codm/static/assets/img/main-slider')

    def __str__(self):
        return '{0}:{1}'.format(self.name, self.show)

class ResponsiveSlider(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='Codm/static/assets/img/main-slider/slider-responsive')

    def __str__(self):
        return '{0}:{1}'.format(self.name, self.show)

class Banner(models.Model):
    code = models.IntegerField(null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    show = models.BooleanField(default=True)
    tp = (
        ('bigbanner', 'بنر بزرگ'),
        ('middlebanner', 'بنر متوسط'),
        ('smallbanner', 'بنر کوچک'),
    )
    Type = models.CharField(max_length=12, choices=tp ,default='smallbanner')
    picture = models.ImageField(upload_to='Codm/static/assets/img/banner')

    def __str__(self):
        return '{0}:{1}:{2}'.format(self.name, self.show, self.Type)

