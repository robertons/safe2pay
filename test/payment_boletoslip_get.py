import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    bankslip = safe2pay.BankSlip()
    retorno = bankslip.ReleaseBankSlip(idTransaction="58187161")

    print(retorno.toJSON())


if __name__ == "__main__":
    main(sys.argv)