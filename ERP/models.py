from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=100)#, blank=True, default='') 
    address = models.TextField() 
    postcode = models.CharField(max_length=6, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.id 

class Contact(models.Model):
    name = models.CharField(max_length=60)
    role = models.CharField(max_length=60, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, default='', null=True)
    office_number = models.CharField(max_length=20, blank=True, default='', null=True)
    email = models.EmailField(max_length=60, blank=True, default='', null=True)
    contact_notes = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
	    return self.name

class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.ManyToManyField(Address)
    contact = models.ManyToManyField(Contact)
    shortname = models.CharField(max_length=20, null=True)
    codename = models.CharField(max_length=5, null=True)
    VAT_Number = models.CharField(max_length=40, blank=True, default='', null=True)
    tax_status = models.CharField(max_length=100, blank=True, default='', null=True)
    office_notes = models.TextField(blank=True, default='', null=True)
    order_notes = models.TextField(blank=True, default='', null=True)
    manufacture_notes = models.TextField(blank=True, default='', null=True)
    delivery_notes = models.TextField(blank=True, default='', null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
	    return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    notes = models.TextField(blank=True, default='')
    print_notes = models.TextField(blank=True, default='')
    cut_notes = models.TextField(blank=True, default='')
    pack_notes = models.TextField(blank=True, default='')
    active = models.BooleanField(default=True)
    SKU = models.CharField(max_length=20, blank=True, default='')
    barcode = models.CharField(max_length=20, blank=True, default='')
    overprint = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    sentinal_text = "---press update to copy STD notes---"
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    Product = models.ManyToManyField(Product)
    delivered = models.BooleanField(default=False, null=True)
    invoiced = models.BooleanField(default=False, null=True)
    paid = models.BooleanField(default=False, null=True)
    pending = models.BooleanField(default=False, null=True)
    out_for_delivery = models.BooleanField(default=False, null=True)
    notes = models.TextField(blank=True, default='', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

 



