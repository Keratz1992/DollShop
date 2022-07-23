from django.shortcuts import render

from dollshop.models import Category, Product


def homepage(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context ={
        'category': category,
        'product': product,
    }
    return render(request, 'dollshop/index.html', context)
