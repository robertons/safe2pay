# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid

from datetime import datetime

def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    items_asssinaturas = safe2pay.Subscription(id="sub_brJdw1jTlTa89zyQ").UpdateItem(safe2pay.Item(**{
            "id": "oi_d478RMAS3bC74PrL",
            "description": "Chaveiro do Tesseract Antigo",
            "status": "active",
            "quantity": 1,
            "pricing_scheme": {
                "price": 3000,
                "scheme_type": "unit"
            }
        }))
    print(items_asssinaturas.toJSON())

if __name__ == "__main__":
    main(sys.argv)
