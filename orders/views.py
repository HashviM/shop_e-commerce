from django.shortcuts import render

def track_order(request):
    return render(request, "orders/track_order.html")
