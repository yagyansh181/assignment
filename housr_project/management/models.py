from django.db import models

# Create your models here.

class Resident(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    building_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    token_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    move_in_date = models.DateField()
    move_out_date = models.DateField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    assigned_groups = models.ManyToManyField('Group')
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField('Permission')
    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=50)
    read = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class CommunityEvent(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    def __str__(self):
        return self.name
