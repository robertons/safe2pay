# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    client = safe2pay.Customer()
    client.name = 'Roberto Neves da Silva'
    client.email = 'robertonsilva@gmail.com'
    client.birthdate = '1982-02-25'
    client.phones = safe2pay.Phones(**{'mobile_phone': { "country_code": 55, "area_code": 27, "number": 999191566}})
    client.Create()

    print(client.toJSON())

if __name__ == "__main__":
    main(sys.argv)
