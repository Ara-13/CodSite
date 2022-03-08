from django.db import models
from django.forms import DateField
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
#important
#from django.conf import settings
#User = settings.AUTH_USER_MODEL
from Users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_number = models.IntegerField(primary_key=True)
    factor_number = models.IntegerField()
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['-order_number']
    
    def __str__(self):
        return 'user:{}; order:{}; factor{}'.format(self.user, self.order_number, self.factor_number)

class CodAccount(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    code = models.IntegerField(primary_key=True)
    pub_date = models.DateField(null=True)
    level = models.IntegerField(default=1)
    
    image = models.ImageField(upload_to='Codm/static/account_pictures', blank=True, null=True)
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

    Status = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('w4p', 'WairForPublish'),
    )

    status = models.CharField(max_length=10, choices=Status, default='w4p')
    final_status = models.CharField(max_length=10, choices=Status, default='w4p')

    price = models.IntegerField()
    
    def __str__(self):
        return '{}---{}---{}---{}T'.format(self.seller, self.code, self.final_status, self.price)
class Video(models.Model):
    account = models.OneToOneField(CodAccount, on_delete=models.CASCADE)
    #video
    #url

class Link(models.Model):
    account = models.ForeignKey(CodAccount, on_delete=models.CASCADE)
    Ts = (
        ('activision' , 'Activision'),
        ('facebook' , 'Facebook'),
        ('gmail' , 'Gmail'),
        ('apple_id' , 'Apple_ID'),
        ('line' , 'Line'),
    )
    Type = models.CharField(max_length=10, choices=Ts, default="Activision")
    mail = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{}-account--{}'.format(self.Type, self.account.code)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    account = models.ManyToManyField(CodAccount, null=True, blank=True)
    S = (
        ('nf', 'NotFinished'),
        ('f', 'Finished')
    )
    status = models.CharField(max_length=2, choices=S, default='nf')

    def __str__(self):
        return 'Cart({})'.format(self.user)
