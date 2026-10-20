# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Volumes/Sandisk/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    card = safe2pay.Card(id="card_MJYE2GDSLHjjkawL").Get(customer_id="cus_bjgeDobsLsEO48nw")
    card.exp_month = 2
    card.exp_year = 2035
    card.billing_address = safe2pay.Address(**{'line_1':'Rua Capitao Domingos Correa da Rocha, 80, Sala 116', 'line_2':'Ed Master Place, Santa Lucia', 'city':'Vitória', 'state':'ES', 'country':'BR', 'zip_code':'29056220'})
    card.Update(customer_id="cus_bjgeDobsLsEO48nw")
    print(card.toJSON())

if __name__ == "__main__":
    main(sys.argv)
