from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

# first, last, email, username. password


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [
#             "flight_id",
#             "airline_id",
#             "departure_city",
#             "arrival_city",
#             "departure_date",
#             "return_date",
#             "class_id",
#             "price",  # Include price if needed
#         ]
