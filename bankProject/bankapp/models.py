from django.db import models
from django.urls import reverse

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=30, blank=True)
    link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    dist = models.ForeignKey(District, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=30, blank=True)


    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name



AccountType= [
    ('savingsAccount', 'Savings Account'),
    ('currentAccount', 'Current Account'),
    ('fixedAccount', 'Fixed Account'),
        ]

Gender= [
    ('female', 'Female'),
    ('male', 'Male'),
         ]

class Data(models.Model):
    name = models.CharField(max_length=250, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20, choices=Gender, default='female')
    phno = models.IntegerField(null=True)
    mail = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=250, blank=True, null=True)
    dist = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    acType = models.CharField(max_length=50, choices=AccountType, default='savingsAccount')
    service = models.TextField(max_length=500, default='creditCard')
    # creditCard = models.BooleanField(default=False,null=True)
    # chequebook = models.BooleanField(default=False,null=True)
    # debitCard = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.name
