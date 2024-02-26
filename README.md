A Project with analytics/databases/Web 
Plotly + Pandas 


Anually
----------------------------------------------------------------
DIAGRAMS
- Gonna put information about each sale assistant's sales anually
in charts

- As well gonna put information about category of items sold
how much each category earned
in charts

- UPT per person
in charts
in the bottom average upt per hole shop

- Monthly revenue for a hole shop
in charts


Daily
----------------------------------------------------------------
INFORMATION
- Top 5 best sellers + their upt
str

-




DIAGRAMS

- Gonna put information about each sale assistant's sales (taken from DB)
in charts



- Monthly revenue for a hole shop
in charts




INFORMATION

- Top 5 best sellers (Their name + number)+ their upt
str

- Gonna put information about category of items sold (Probably manual or automatic generation of category)
how much each category earned 
str



DB info
----------------------------------------------------------------
Person sale assistant
- Sale assistant name + number (FK2) ---one to one---
[//]: # (- Amount of transaction &#40;automatic&#41;)
- Transaction number (FK1)  ---many to many---
- Days worked (Probably when have some transactions per day)

For transaction
- Transaction number (FK1) ---many to many---
- Sale assistant (FK2) ---one to one---
- Customer number (FK3) ---one to one---
- Amount of money
- Items per transaction
- Date 

Customer 
- Customer name 
- Customer Number (FK3) ---one to one---
- Transaction (FK1) ---many to many---
- Date registration 
