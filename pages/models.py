from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)
    week_number = models.CharField(max_length=2, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        print(self.start_date.isocalendar()[1])
        if self.week_number == "":
            self.week_number = self.start_date.isocalendar()[1]
        super().save(*args,**kwargs)


class Sale_assistant(models.Model):
    # sale_assistant = models.ForeignKey() #one to one
    # transaction_number = models.ForeignKey() #many to many
    # days_worked = models.DateField() ????
    ...

    def __str__(self):
        return f""

class Transaction(models.Model):
    transaction_number = models.IntegerField() #many to many
    # sale_assistant = models.ForeignKey() #one to one
    customer_number = models.CharField(max_length=100) #one to one
    amount_of_money = models.FloatField()
    items_per_transaction = models.IntegerField()
    date = models.DateField()


    def __str__(self):
        return f"Transaction: \ncustomer:{str(self.customer_number)} \nAmount of money{str(self.amount_of_money)} \nItems per transaction{str(self.items_per_transaction)}\n Date{str(self.date)}"


class Customer(models.Model):
    customer_name = models.CharField()
    # customer_number = models.ForeignKey()
    # transaction = models.ForeignKey()
    date_registred = models.DateField()