original_price = 100
discounted_price = original_price * .80
print(discounted_price)

score = 55
extra_credit = 10

if score >= 60 or extra_credit >=10:
    print("Pass")
    
grade = 85

if grade >=90:
    print("A")
elif grade >=80:
    print("B")
elif grade >=80:
    print("C")
else:
    print("F")
    
month = 7
if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Fall")
    
price = 45.99
budget = 50

if price <= budget:
    print("Can afford")
else:
    print("Too expensive")
    
age = 25
has_license = True
has_car = True

if age and has_license and has_car:
    print("Can drive")
else:
    print("Can't drive")
    
for number in range(1, 6):
    print(number ** 2)
    
for i in range(1,11):
    number = 7 * i
    print(number)