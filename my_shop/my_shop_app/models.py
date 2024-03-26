from django.db import models
import base64

class Category(models.Model):
    objects = None
    title = models.CharField(max_length=190)

    def __str__(self):
        return self.title

class Products(models.Model):
    objects = None
    title = models.CharField(max_length=190)
    image = models.ImageField(upload_to="images/")
    base_64 = models.CharField(max_length=50000, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    info = models.TextField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    amount = models.PositiveIntegerField(default=5)
    status = models.BooleanField()


    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Products, self).save()

    def __str__(self):
        return self.title

class Order(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)



    def __str__(self):

        return f"{self.name} {self.surname}"

class User_register(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Username} {self.Password} {self.phone}"

class User_login(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)