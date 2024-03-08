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


Info about customer
----------------------------------------------------------------
We have place to enter customer number to find
information about his/her 
data + history of transaction 
- place to enter number 
- button to find

If customer not found ask to do a registration(Maybe)


Add Transaction, Page 
----------------------------------------------------------------
We have place to put 
- Amount of money 
- Number of Sale Assistant
(if num is not found exception Error)

- Number of customer 
(if num is not found, button to register a customer appears and text
'Please register and back')
(the page after pressing a button opens on a new page)

- amount of items sold 
- date (no more than today )


Registration of customer, Page
----------------------------------------------------------------
We can do a registration via admin or vir this page which presents registration page
We have place to put info 
- Name (necessary!)
- Surname (necessary!)
- Date of Birthday (not necessary)
- Address (not necessary)
- E-mail (necessary!)


DB info
----------------------------------------------------------------
Person sale assistant
- Sale assistant name + number (FK2) ---one to one--- (main)
[//]: # (- Amount of transaction &#40;automatic&#41;)
- Transaction number (FK1)  ---one to many---
- Days worked (Probably when have some transactions per day)

For transaction
- Transaction number (FK1) ---one to many---(main)
- Sale assistant (FK2) ---one to one---
- Customer number (FK3) ---one to one---
- Amount of money
- Items per transaction
- Date 

Customer 
- Customer name 
- Customer Number (FK3) ---one to one---(main)
- Transaction number (FK1) ---one to many---


all next info mostly for registration and not necessary to be given
- Date registration 
- Gender (choices)
- E-mail
- Address
- Post Code
- Additional details



