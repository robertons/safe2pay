# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid

from datetime import datetime

def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    safe2pay.Plan(id="plan_brJdw1jTlTa89zyQ").DeleteItem("pi_d478RMAS3bC74PrL")
    print(items_asssinaturas.toJSON())

if __name__ == "__main__":
    main(sys.argv)
