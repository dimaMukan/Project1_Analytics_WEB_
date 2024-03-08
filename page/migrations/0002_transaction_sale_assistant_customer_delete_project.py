# Generated by Django 5.0.2 on 2024-03-03 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.IntegerField()),
                ('amount_of_money', models.FloatField()),
                ('items_per_transaction', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sale_assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_assistant_name', models.CharField(blank=True, max_length=100)),
                ('sale_assistant_surname', models.CharField(blank=True, max_length=100)),
                ('sale_assistant_number', models.IntegerField()),
                ('transaction_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=100)),
                ('customer_number', models.IntegerField()),
                ('date_registered', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('House_number', models.IntegerField(blank=True)),
                ('Post_Code', models.CharField(blank=True, max_length=15)),
                ('Additional_details', models.CharField(blank=True, max_length=100)),
                ('transaction_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='page.transaction')),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
