import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    singleSale = safe2pay.SingleSale()
    retorno = singleSale.CancelSingleSale("eaf69aafca4d4e01921c356222808c1f")

    print(retorno.toJSON())


if __name__ == "__main__":
    main(sys.argv)