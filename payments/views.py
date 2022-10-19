import stripe
from django.conf import settings
from django.views import View
from cart.views import *

"""
Оплата товара через Stripe
---------------------------------------------------------------------
Получаем ключ, который задан из файла settings.
Далее получаем информацию о товаре, его стоимость, название и количество,
устанавливает оплату в рублях, метод оплаты - карта.
В случае оплаты, перенаправляем на url/success/
В случае отмены идет перенаправление на url/cancel/
"""
stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        product.quantity = request.POST.get('quantity')
        print(product.quantity)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'rub',
                        'unit_amount': int(product.price * 100),
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': product.quantity,
                },
            ],
            metadata={
                "product_id": product.id,
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success-payment/',
            cancel_url=YOUR_DOMAIN + '/cancel-payment/',
        )

        return redirect(checkout_session.url, code=303)

