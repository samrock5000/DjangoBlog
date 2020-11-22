#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, jsonify, request

import stripe
# This is your real test secret API key.
stripe.api_key = 'sk_test_51HdKOyJ1xIq3bW1YSD4hL51kA88Bvtdrj67PiIuaRjm6OZo3vRe8KcyPUW5EfDkRii18RTSRq7RDeC4Dj08QrEgL000qMXUbup'

app = Flask(__name__,
            static_url_path='',
            static_folder='.')

YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/create-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(port=4242)
