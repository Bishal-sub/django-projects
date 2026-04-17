from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productname = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
 

    def __str__(self):
        return self.productname


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    stock = models.PositiveIntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.product.productname} - {self.size.name} - {self.color.name}'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.product.productname
    

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.variant.price