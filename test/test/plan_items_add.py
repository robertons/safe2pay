# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid

from datetime import datetime

def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    items_plano = safe2pay.Plan(id="plan_1VRDB5AfWfjBnZpx").AddItem(safe2pay.Item(**{
            "description": "Chaveiro do Bacana",
            "quantity": 4,
            "pricing_scheme": {
                "price": 2000,
                "scheme_type": "unit"
            }
        }))

    print(plano.toJSON())

if __name__ == "__main__":
    main(sys.argv)
