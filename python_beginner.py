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