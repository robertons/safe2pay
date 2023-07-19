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
    
    pageNumber = 1
    rowsPerPage = 50
    
    response = chargeback.ListChargebacks(pageNumber, rowsPerPage)
    print(f'Retorno ListChargebacks: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)