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
    sale_assistant = models.OneToOneField(page.models.Sale_assistant, on_delete=models.SET_NULL) #one to one
    customer_number = models.OneToOneField(page.models.Customer, on_delete=models.SET_NULL) #one to one
    amount_of_money = models.FloatField()
    items_per_transaction = models.IntegerField()
    date = models.DateField()


    def __str__(self):
        return f"Transaction: \ncustomer:{str(self.customer_number)} \nAmount of money{str(self.amount_of_money)} \nItems per transaction{str(self.items_per_transaction)}\n Date{str(self.date)}"

class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    Genders = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    customer_name = models.CharField()
    customer_number = models.IntegerField()
    transaction_number = models.ForeignKey(Transaction,on_delete=models.CASCADE, null=True)
    date_registered = models.DateField()
    gender = models.CharField(max_length=1,choices=Genders, default=MALE)
    email = models.EmailField()

    def __str__(self):
        return f""


class Sale_assistant(models.Model):
    sale_assistant_name = models.CharField()
    sale_assistant_surname = models.CharField()

    sale_assistant_number = models.IntegerField() #one to one
    transaction_number = models.ForeignKey(Transaction, on_delete=models.CASCADE) #one to many
    # days_worked = models.DateField() ????
    ...

    def __str__(self):
        return f""


