from django.shortcuts import redirect, render

from main.models import Category, Dish, Order, DishInOrder
def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'home.html', context)

def add_to_order(request, dish_id):
    # Логіка для додавання страви до замовлення
    if request.method == 'POST':
        # Тут можна реалізувати логіку додавання страви до замовлення
        dish = Dish.objects.get(id=dish_id)
        cart = request.session.get('cart', {})
        if str(dish_id) in cart:
            cart[str(dish_id)] += 1
        else:
            cart[str(dish_id)] = 1
        request.session['cart'] = cart
    return redirect('home')

def view_cart(request):
    cart = request.session.get('cart', {})
    dishes_in_cart = []
    total_price = 0

    for dish_id, quantity in cart.items():
        dish = Dish.objects.get(id=dish_id)
        dishes_in_cart.append({
            'dish': dish,
            'quantity': quantity,
            'total_price': dish.price * quantity
        })
        total_price += dish.price * quantity

    context = {
        'dishes_in_cart': dishes_in_cart,
        'total_price': total_price
    }
    return render(request, 'cart.html', context)

# Create your views here.
