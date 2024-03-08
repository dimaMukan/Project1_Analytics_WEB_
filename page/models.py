from django.db import models
from django.contrib.auth.models import User

import page


# class Project(models.Model):
#     name = models.CharField(max_length=200)
#     start_date = models.DateField()
#     responsible = models.ForeignKey(User, on_delete=models.CASCADE)
#     week_number = models.CharField(max_length=2, blank=True)
#     end_date = models.DateField()
#
#     def __str__(self):
#         return str(self.name)
#
#     def save(self,*args,**kwargs):
#         print(self.start_date.isocalendar()[1])
#         if self.week_number == "":
#             self.week_number = self.start_date.isocalendar()[1]
#         super().save(*args,**kwargs)




class Transaction(models.Model):
    transaction_number = models.IntegerField() #one to many(main)
    amount_of_money = models.FloatField()
    items_per_transaction = models.IntegerField()
    date = models.DateField()


    def __str__(self):
        return f'{str(self.transaction_number)}'


class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    Genders = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    customer_name = models.CharField(max_length=100,blank=True)
    customer_number = models.IntegerField()
    transaction_number = models.ForeignKey(Transaction,on_delete=models.CASCADE, null=True,blank=True)

    date_registered = models.DateField()
    gender = models.CharField(max_length=1,choices=Genders, default=MALE)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100,blank=True)
    House_number = models.IntegerField(blank=True,null=True)
    Post_Code = models.CharField(max_length=15,blank=True)
    Additional_details = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f""


class Sale_assistant(models.Model):

    sale_assistant_name = models.CharField(max_length=100,blank=True)
    sale_assistant_surname = models.CharField(max_length=100,blank=True)

    sale_assistant_number = models.IntegerField() #one to one
    transaction_number = models.ForeignKey(Transaction, on_delete=models.CASCADE) #one to many
    # days_worked = models.DateField() ????


    def __str__(self):
        return f""


