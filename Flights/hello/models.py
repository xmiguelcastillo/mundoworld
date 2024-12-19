from turtle import mode

from django.db import models
from django.utils import timezone


class Customer(models.Model):
    """Model representing a flight booking by a customer."""

    # flight_id = models.CharField(max_length=10, unique=True)
    # airline_id = models.CharField(max_length=10)
    # departure_city = models.CharField(
    #     max_length=50
    # )  # Increased length for city names
    arrival_city = models.CharField(
        max_length=50
    )  # Increased length for city names
    # departure_date = models.DateField()
    # return_date = models.DateField(blank=True, null=True)
    #
    # class_id = models.CharField(
    #     max_length=10,
    #     choices=[
    #         ("economy", "Economy Class Flights"),
    #         ("premium", "Premium Class Flights"),
    #         ("business", "Business Class Flights"),
    #         ("first", "First Class Flights"),
    #     ],
    # )
    #
    # price = models.IntegerField(default=0)  # Added default value

    def __str__(self) -> str:
        return f"{self.arrival_city}"
