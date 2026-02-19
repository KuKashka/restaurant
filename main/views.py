from django.shortcuts import render

from main.models import Category
def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'home.html', context)

# Create your views here.
