# string input
customer_name = input()
location = input()

# int input
quantity = int(input())

# float input
price = float(input())

# list input 
items = input().split(",")

# set input 
coupons = set(input().split(","))

# tuple input
delivery_time_slots = tuple(input().split(","))

# dictionary input 
raw_dict = input()
payment_details = {}

for pair in raw_dict.split(","):
    key, value = pair.split(":")
    payment_details[key] = value

# Calculations
total_amount = quantity * price

# OUTPUT
print("Customer Name:", customer_name)
print("Location:", location)
print("Quantity:", quantity)
print("Price:", price)
print("Items List:", items)
print("Coupons Set:", coupons)
print("Delivery Slots Tuple:", delivery_time_slots)
print("Payment Details Dictionary:", payment_details)
print("Total Bill:", total_amount)
