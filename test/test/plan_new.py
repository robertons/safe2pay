# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid

from datetime import datetime

def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    plano = safe2pay.Plan()
    plano.name = "Plano Mensal Teste"
    plano.description = "Plano de teste de integração API"
    plano.shippable = False
    plano.payment_methods.add('credit_card')
    plano.statement_descriptor = 'Assinatura'
    plano.currency = 'BRL'
    plano.interval = 'month'
    plano.interval_count = 1
    plano.billing_type = 'prepaid'
    plano.quantity = 1
    plano.pricing_scheme = safe2pay.PricingScheme(**{
            "scheme_type": "unit",
            "price": 5000,
            "minimum_price": 5000,
        })
    plano.Create()

    print(plano.toJSON())

if __name__ == "__main__":
    main(sys.argv)
