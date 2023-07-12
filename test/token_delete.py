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

    response = token.DeleteToken('145a2a0a8ccd4547b7514fcd93af50a0')
    print(f'Retorno DeleteToken: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)