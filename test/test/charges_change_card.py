# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Volumes/Sandisk/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    cobranca = safe2pay.Charge(id="ch_Pr5R4D5izhEbyNQY").ChangeCard(safe2pay.Card(
        first_six_digits = "400000",
        last_four_digits = "0010",
        brand = "Mastercard",
        holder_name = "Tony Stark",
        holder_document = "93095135270",
        number = "4000000000000010",
        exp_month = 1,
        exp_year = 2030,
        cvv = 123,
        billing_address = safe2pay.Address(**{
          "zip_code": "22000111",
          "city": "Rio de Janeiro",
          "state": "RJ",
          "country": "BR",
          "line_1": "375, Av. General Osorio, Centro",
          "line_2": "7º Andar"
        })))
    print(cobranca.toJSON())

if __name__ == "__main__":
    main(sys.argv)
