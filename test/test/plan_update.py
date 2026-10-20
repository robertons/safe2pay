# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    plano = safe2pay.Plan(id="plan_ODjw15Af9WUgzwkg").Get()
    plano.statement_descriptor = "AST Test"
    plano.Update()
    print(plano.toJSON())

if __name__ == "__main__":
    main(sys.argv)
