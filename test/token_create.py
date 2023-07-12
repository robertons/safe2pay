import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_sandbox, '', True, True)

    token = safe2pay.Token()
    token.IsSandbox = True
    token.Holder = 'Elaine C Rocha'
    token.CardNumber = '5162923909165637'
    token.ExpirationDate = '07/2024'
    token.SecurityCode = '645'

    response = token.CreateToken()
    print(f'Retorno CreateToken: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)