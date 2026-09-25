from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expense_model(models.Model):
    
    CATEGORY_CHOICES = [
    ("food", "Food"),
    ("groceries", "Groceries"),
    ("transportation", "Transportation"),
    ("fuel", "Fuel"),
    ("rent", "Rent"),
    ("utilities", "Utilities"),
    ("electricity", "Electricity"),
    ("water", "Water"),
    ("internet", "Internet"),
    ("phone", "Phone"),
    ("healthcare", "Healthcare"),
    ("medicine", "Medicine"),
    ("insurance", "Insurance"),
    ("education", "Education"),
    ("shopping", "Shopping"),
    ("clothing", "Clothing"),
    ("entertainment", "Entertainment"),
    ("subscriptions", "Subscriptions"),
    ("travel", "Travel"),
    ("hotel", "Hotel"),
    ("personal_care", "Personal Care"),
    ("fitness", "Fitness & Gym"),
    ("sports", "Sports"),
    ("gifts", "Gifts"),
    ("donations", "Donations"),
    ("family", "Family"),
    ("pets", "Pets"),
    ("home", "Home & Furniture"),
    ("electronics", "Electronics"),
    ("maintenance", "Maintenance"),
    ("taxes", "Taxes"),
    ("fees", "Fees & Charges"),
    ("debt_payment", "Debt Payment"),
    ("loan", "Loan"),
    ("investment", "Investment"),
    ("savings", "Savings"),
    ("business", "Business"),
    ("work", "Work"),
    ("books", "Books"),
    ("coffee", "Coffee"),
    ("restaurants", "Restaurants"),
    ("alcohol", "Alcohol"),
    ("other", "Other"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=55)
    category = models.CharField(choices=CATEGORY_CHOICES)
    description = models.TextField()
    amount = models.IntegerField()

    