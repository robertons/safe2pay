import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    plan = safe2pay.PlanSubscription()
    plan.Token = "8639c75f65eb45aba8688cac9b43af68"
    
    response = plan.UpdateTokenCard("10265")
    print(f'Retorno UpdateTokenCard: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)