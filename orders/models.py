from django.db import models

# Create your models here.


class CommonInfo(models.Model):
    name = models.CharField(max_length=32)
    small_price = models.FloatField(blank=True)
    large_price = models.FloatField()

    class Meta:
        abstract = True


class ToppingsAndExtras(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()


class Pizza(CommonInfo):
    pizza_type = models.CharField(max_length=32)  # Regular of Sicilian
    available_toppings = models.ManyToManyField(ToppingsAndExtras)
    max_toppings = models.IntegerField()


class Sub(CommonInfo):
    available_toppings = models.ManyToManyField(ToppingsAndExtras)


class OtherDish(CommonInfo):
    pass
