# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    transfersetting = safe2pay.Recipient(id="rp_WGAn6Q4SySWZBlRy").ChangeTransferSettings(transfer_enabled=True, transfer_interval="monthly", transfer_day="1")
    print(transfersetting.toJSON())

if __name__ == "__main__":
    main(sys.argv)
