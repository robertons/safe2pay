import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    parcelamento = safe2pay.InstallmentValue()
    amount = 12345.67
    retorno = parcelamento.GetInstallmentValues(amount)

    print(retorno.toJSON())


if __name__ == "__main__":
    main(sys.argv)
    
