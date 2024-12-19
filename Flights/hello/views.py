from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import CreateUserForm


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")  # Use parentheses
        password = request.POST.get("password")  # Use parentheses

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/hello")  # Redirect after successful login
        else:
            messages.error(
                request, "Invalid username or password."
            )  # Provide feedback on failure

    return render(request, "hello/loginPage.html")


def logoutPage(request):
    logout(request)
    return redirect("/hello/loginPage")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            # messages.success(request, "Profle details Updated.")
            return redirect("loginPage")
    return render(request, "hello/register.html", {"form": form})


def index(request):
    # if request.method == "POST":
    #     departure = request.POST.get("departure")
    #     destination = request.POST.get("destination")
    #     leaving = request.POST.get("leaving")
    #     return_date = request.POST.get("return")
    #     class_id = request.POST.get("class_id")
    #
    #     flight_search_input = FlightSearch(  # Adjust the model name
    #         departure=departure,
    #         destination=destination,
    #         leaving=leaving,
    #         return_date=return_date,
    #         class_id=class_id,
    #     )
    #
    #     try:
    #         flight_search_input.save()
    #         # Redirect to a success page or another page after saving
    #         return redirect(
    #             "success_page"
    #         )  # Replace 'success_page' with your desired URL pattern name
    #     except Exception as e:
    #         # Handle error (log it, show a message, etc.)
    #         print(f"Error saving flight search: {e}")

    return render(request, "hello/index.html")


#


def flights(request):
    arrival_city = Customer.all()

    return render(request, "hello/flights.html", {"arrival_city": arrival_city})


# def flights(request):
#     departure_cities = Customer.objects.values_list(
#         "departure_city", flat=True
#     ).distinct()  # Get unique departure cities
#
#     if request.method == "POST":
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             # Here you can process the form data if needed, but for now, we'll just show the cities
#             return redirect("flights")  # Redirect to the same view to refresh
#
#     else:
#         form = CustomerForm()
#
#     return render(
#         request,
#         "hello/flights.html",
#         {"form": form, "departure_cities": departure_cities},
#     )
