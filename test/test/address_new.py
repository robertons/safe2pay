# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Volumes/Sandisk/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    address = safe2pay.Address(**{
      "zip_code": "22000111",
      "city": "Rio de Janeiro",
      "state": "RJ",
      "country": "BR",
      "line_1": "375, Av. General Osorio, Centro",
      "line_2": "7º Andar"
    })
    address.Create(customer_id='cus_bjgeDobsLsEO48nw')
    print(address.toJSON())

if __name__ == "__main__":
    main(sys.argv)
