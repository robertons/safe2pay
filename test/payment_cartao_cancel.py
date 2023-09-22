import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    boleto = safe2pay.CreditCard().CancelCredit('64356803','1')
    
    print(f'Retorno CancelCredit: {boleto.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)