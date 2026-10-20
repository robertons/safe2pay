# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    pedido = safe2pay.Order()
    pedido.customer_id = "cus_bjgeDobsLsEO48nw"
    pedido.code =  "62LVFN7I4R"
    pedido.amount = 2900
    pedido.currency =  "BRL"
    pedido.items.add(safe2pay.Item(**{
            "id": "oi_d478RMAS3bC74PrL",
            "description": "Chaveiro do Tesseract",
            "amount": 2900,
            "quantity": 1,
            "status": "active",
            "code":"abc"
        }))

    pedido.shipping = safe2pay.Shipping(**{
        "amount": 100,
        "description": "Stark",
        "recipient_name": "Tony Stark",
        "recipient_phone": "24586787867",
        "address": {
            "line_1": "10880, Malibu Point, Malibu Central",
            "zip_code": "90265",
            "city": "Malibu",
            "state": "CA",
            "country": "US"
        }})

    pedido.payments.add(safe2pay.Payment(**{
         "amount" : 3000,
         "payment_method":"checkout",
         "checkout": {
            "expires_in":120,
            "billing_address_editable" : False,
            "customer_editable" : False,
            "accepted_payment_methods": ["credit_card"],
            "success_url": "https://www.pagar.me",
         }
         }))

    pedido.Create()

    print(pedido.toJSON())

if __name__ == "__main__":
    main(sys.argv)
