from django.shortcuts import render

def product_list(request):
    return render(request, "shop/product_list.html")

def product_detail(request, pk):
    return render(request, "shop/product_detail.html", {"pk": pk})
