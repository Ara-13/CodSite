from django.db import models
from Users.models import User

class Group(models.Model):
    tag = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='Products/media/Products/product-logos/', max_length=5000, null=True)
    background = models.ImageField(upload_to='Products/media/Products/product-backgrounds/', max_length=5000, null=True)
    description = models.TextField(max_length=900, null=True)

    facebook = models.BooleanField(default=False)
    gmail = models.BooleanField(default=False)
    apple = models.BooleanField(default=False)
    activition = models.BooleanField(default=True)
    supercell = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class EP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    Ts = (
        ('activision' , 'اکتیویژن'),
        ('facebook' , 'فیسبوک'),
        ('gmail' , 'جیمیل'),
        ('apple' , 'اپل آی-دی'),
        ('supercell' , 'سوپرسل'),
    )
    Type = models.CharField(max_length=10, choices=Ts, default="Activision")

class Product(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    ep = models.ManyToManyField(EP, blank=True)

    code = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=900, null=True, blank=True)

    image = models.ImageField(upload_to='Products/media/Products/product_picture/{}/'.format(group.name), max_length=5000, null=True)

    S = (
        ('AV', 'Available'),
        ('NA', 'NotAvailable'),
    )
    status = models.CharField(max_length=2, choices=S, default='AV')

    price = models.IntegerField(default=30000)

    def __str__(self):
        return '{};{};{}تومان'.format(self.group, self.name, self.price)