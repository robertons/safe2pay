import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    chargeback = safe2pay.Chargeback()
    
    idChargeback = 1
    idTransaction = 50
    
    response = chargeback.GetChargeback(idChargeback, idTransaction)
    print(f'Retorno GetChargeback: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)