# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    assinatura = safe2pay.Subscription()
    assinatura.code = '1234'
    assinatura.customer_id = "cus_bjgeDobsLsEO48nw"
    assinatura.plan_id = "plan_VR92ne8UEUGWNMAa"
    assinatura.interval = 'month'
    assinatura.interval_count = 1
    assinatura.currency = 'BRL'
    assinatura.payment_method = "credit_card"
    assinatura.billing_type = 'prepaid'
    assinatura.installments = 1
    assinatura.statement_descriptor = "AST Gofans"    
    assinatura.card = safe2pay.Card(**{
        "number": "4000000000000010",
        "holder_name": "Tony Stark",
        "exp_month": 1,
        "exp_year": 30,
        "cvv": "3531",
        "billing_address": {
            "line_1": "10880, Malibu Point, Malibu Central",
            "zip_code": "90265",
            "city": "Malibu",
            "state": "CA",
            "country": "US"
        }
    })

    assinatura.Create()

    print(assinatura.toJSON())

if __name__ == "__main__":
    main(sys.argv)
