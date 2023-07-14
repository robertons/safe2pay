import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    singleSale = safe2pay.SingleSale()
    retorno = singleSale.GetSingleSale("311d449af28b4df0a8ff4f0226473056")

    print(retorno.toJSON())


if __name__ == "__main__":
    main(sys.argv)