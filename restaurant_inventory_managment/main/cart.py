class Cart():
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += 1
        else:
            self.cart[product_id] = {'quantity': 1, 'price': str(product.price_entry)}

        self.session['cart'] = self.cart
        self.session.modified = True

    def __len__(self):
        # Sumar las cantidades de los elementos en el carrito y los elementos seleccionados
        cart_quantity = sum(item['quantity'] for item in self.cart.values())
        return cart_quantity