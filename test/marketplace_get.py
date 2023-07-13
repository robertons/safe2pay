import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_sandbox, '', True, True)

    marketplace = safe2pay.Marketplace()

    response = marketplace.GetSubAccount('123456')
    print(f'Retorno GetSubAccount: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)