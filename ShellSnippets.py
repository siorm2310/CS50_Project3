import csv
from orders.models import Sub, OtherDish

with open(r"C:\CS50_Course\CS50_Project3\other.csv") as f:
    reader = csv.readers
        new_object = OtherDish(
            dish_type=row[0], name=row[1],large_price=row[3]
        )
        try:
            new_object.save()
        except:
            print(f"error with {row}")


for top in ToppingsAndExtras.objects.all():
    print(top)

for sub in Sub.objects.all():
    sub.available_toppings.add(extra_cheese)

