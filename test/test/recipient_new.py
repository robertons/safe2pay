# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    recebedor = safe2pay.Recipient()
    recebedor.name = 'Roberto Neves da Silva'
    recebedor.email = "joaodasilva@gmail.com"
    recebedor.document = '09292800752'
    recebedor.description = 'Recebedor teste de cadastro'
    recebedor.type = 'individual'
    recebedor.default_bank_account = safe2pay.BankAccount(**{
        "holder_name": "Roberto Neves da Silva",
        "holder_type": "individual",
        "holder_document": '09292800752',
        "bank": "033",
        "type": "checking",
        "branch_number": "4316",
        "branch_check_digit": "0",
        "account_number": "01001647",
        "account_check_digit": "3",
    })
    recebedor.Create()
    print(recebedor.toJSON())

if __name__ == "__main__":
    main(sys.argv)
