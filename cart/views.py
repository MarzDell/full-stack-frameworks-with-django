from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, 'cart.html')


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    if request.POST.get('quantity') != '':
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect(reverse('products'))
    else:
        return redirect(reverse('products'))


def adjust_cart(request, id):
    """Adjust the quantity of the specified product to the specified amount"""
    if request.POST.get('quantity') != '':
        quantity = int(request.POST.get('quantity', default=0))
        cart = request.session.get('cart', {})

        if quantity > 0:
            cart[id] = quantity
        else:
            cart.pop(id)

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))
    else:
        return redirect(reverse('products'))

