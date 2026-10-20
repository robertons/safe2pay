# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Volumes/Sandisk/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    cobranca = safe2pay.Charge(id="ch_Pr5R4D5izhEbyNQY").ChangePaymentMethod(safe2pay.Payment(**{
         "amount" : 3000,
         "payment_method":"credit_card",
         "credit_card": {
            'card_id': "card_G4QnR6ck7cgBn8XR",
         }
    }))
    print(cobranca.toJSON())

if __name__ == "__main__":
    main(sys.argv)
