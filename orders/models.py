from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=32)
    small_price = models.FloatField(blank=True, null=True)
    large_price = models.FloatField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class ToppingsAndExtras(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class Pizza(CommonInfo):
    PIZZA_TYPES = [("REG", "Regular"), ("SIC", "Sicilian")]
    pizza_type = models.CharField(
        max_length=3, choices=PIZZA_TYPES, default="REG"
    )  # Regular of Sicilian
    available_toppings = models.ManyToManyField(ToppingsAndExtras, blank=True)
    max_toppings = models.IntegerField()


class Sub(CommonInfo):
    available_toppings = models.ManyToManyField(ToppingsAndExtras, blank=True)


class OtherDish(CommonInfo):
    dish_type = models.CharField(max_length=32, default="")
