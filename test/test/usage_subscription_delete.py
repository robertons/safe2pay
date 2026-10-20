# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projects/safe2pay')

import safe2pay

import uuid


def main(arg):
    safe2pay.Safe2Pay('acc_L3vxGpMF71h56nyK','pk_test_Y479512hrHMQ956j', 'sk_test_nDjEyXohVeSVA0Nl', sandbox=True, debug=True)


    safe2pay.Usage(id="usage_2VBDB53fWfjgnZpX").Delete(subscription_id="sub_1VRDB5AfWfjBnZpx", item_id="si_QjGb0BZUkUD0Eyag")


if __name__ == "__main__":
    main(sys.argv)
