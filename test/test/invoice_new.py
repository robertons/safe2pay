# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    fatura = safe2pay.Invoice().Create(subscription_id='sub_brJdw1jTlTa89zyQ', cycle_id='cycle_v0dxrO3i2iyr5J9X')
    print(fatura.toJSON())

if __name__ == "__main__":
    main(sys.argv)
