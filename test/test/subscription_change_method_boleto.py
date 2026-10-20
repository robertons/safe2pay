# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    cobranca = safe2pay.Subscription(id="sub_Gdg4m3BTrqTyoK01").ChangePaymentMethod(safe2pay.Payment(**{
         "payment_method":"boleto",
         "boleto": {
            "instructions": "Instrução de boleto de teste",
            "due_at" : "2022-10-24T14:30:22",
            "document_number" : "123456",
            "type": "DM"
         }
    }))
    print(cobranca.toJSON())

if __name__ == "__main__":
    main(sys.argv)
