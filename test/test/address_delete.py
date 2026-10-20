# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Volumes/Sandisk/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)

    safe2pay.Address(id="addr_lOAgNqH1wCxD6eYd").Delete(customer_id="cus_bjgeDobsLsEO48nw")


if __name__ == "__main__":
    main(sys.argv)
