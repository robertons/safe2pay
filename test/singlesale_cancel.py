import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    singleSale = safe2pay.SingleSale()
    retorno = singleSale.CancelSingleSale("9690aa72a6204c5da78bae281c4da991")

    print(retorno.toJSON())


if __name__ == "__main__":
    main(sys.argv)