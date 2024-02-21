
from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 0.15  # 15% tax rate

def default_view(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")

def calculate_tax(request, price):
    try:
        price = float(price)
        total = price * (1 + tax_rate)
        return HttpResponse(f"<h1>Total price with tax: ${total:.2f}</h1>")
    except ValueError:
        return HttpResponse("<h1>Invalid input. Please provide a valid number.</h1>")

def tax_rate_view(request):
    return render(request, 'taxapp/tax_rate.html', {'tax_rate': tax_rate})
