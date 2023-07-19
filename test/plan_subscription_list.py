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
     
    pageNumber = 1
    rowsPerPage = 50
    customerName = None
    status = None
    initialDate = None
    endDate = None
    idPlan = None
    
    response = plan.ListSubscriptions(pageNumber, rowsPerPage, customerName, status, initialDate, endDate, idPlan)
    print(f'Retorno ListSubscriptions: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)