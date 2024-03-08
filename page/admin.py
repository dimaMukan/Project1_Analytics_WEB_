from django.contrib import admin
from .models import Transaction,Customer,Sale_assistant

class Transaction_display(admin.ModelAdmin):
    list_display = ['transaction_number','amount_of_money','items_per_transaction']

class Customer_display(admin.ModelAdmin):
    list_display = ['customer_name','email','gender','transaction_number']

class Sale_assistant_display(admin.ModelAdmin):
    list_display = ['sale_assistant_name','sale_assistant_surname']

admin.site.register(Transaction,Transaction_display)
admin.site.register(Customer,Customer_display)
admin.site.register(Sale_assistant,Sale_assistant_display)
