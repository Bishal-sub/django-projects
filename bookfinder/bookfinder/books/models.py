from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):

    BOOK_LIST = [
        ('python', 'Python Programming'),
        ('django', 'Django Development'),
        ('ml', 'Machine Learning'),
        ('ai', 'Artificial Intelligence'),
        ('db', 'Database Systems'),
    ]

    category = models.CharField(choices=BOOK_LIST,max_length=50)
    name = models.CharField(max_length=50)
    author = models.CharField( max_length=50)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)
    img = models.ImageField( upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.name

#one to many    
class BooksReviews(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE,related_name='bookreview')
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    
    rating = models.IntegerField(choices=[
    ('1', '1 star'),
    ('2', '2 stars'),
    ('3', '3 stars'),
    ('4', '4 stars'),
    ('5', '5 stars'),
    ])
    


#many to many

class bookstore(models.Model):
    name = models.CharField( max_length=50)
    location = models.CharField( max_length=50)
    books = models.ManyToManyField(Books, related_name="store")
    
    
#one to one    
class ISBN(models.Model):
    name = models.OneToOneField(Books,  on_delete=models.CASCADE, related_name='isbn')
    isbn_number = models.IntegerField()
    pages = models.IntegerField()
    
    def __str__(self):
        return self.name.name
    