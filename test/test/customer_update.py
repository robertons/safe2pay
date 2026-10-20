# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    client = safe2pay.Customer(id='cus_bjgeDobsLsEO48nw').Get()
    client.address = safe2pay.Address(line_1='Rua Capitao Domingos Correa da Rocha, 80, Sala 116', line_2='Ed Master Place, Santa Lucia', city='Vitoria', state='ES', country='BR', zip_code='29056220')
    client.document = "09292800752"
    client.document_type = "CPF"
    client.type = "individual"
    client.Update()

    print(client.toJSON())

if __name__ == "__main__":
    main(sys.argv)
