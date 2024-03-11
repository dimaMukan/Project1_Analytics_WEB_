from django.contrib import admin
from .models import Transaction,Customer,Sale_assistant

@admin.register(Transaction)
class Transaction_display(admin.ModelAdmin):
    list_display = ['transaction_number','amount_of_money','items_per_transaction']

@admin.register(Customer)
class Customer_display(admin.ModelAdmin):
    list_display = ['customer_name','email','gender','transaction_number']

@admin.register(Sale_assistant)
class Sale_assistant_display(admin.ModelAdmin):
    list_display = ['sale_assistant_name','sale_assistant_surname']
    list_editable = ['sale_assistant_surname']
    ordering = []

# admin.site.register(Transaction,Transaction_display)
# admin.site.register(Customer,Customer_display)
# admin.site.register(Sale_assistant,Sale_assistant_display)
