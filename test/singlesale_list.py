import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    singleSale = safe2pay.SingleSale()

    pageNumber = 1 
    rowsPerPage = 10 
    dateInitial = '01/07/2023'
    dateEnd = '20/07/2023'
    objReference = None
    objCustomerName = None
    objCustomerIdentity = None
    objTransactionStatus = None


    retorno = singleSale.ListSingleSales(
        pageNumber, 
        rowsPerPage, 
        dateInitial,
        dateEnd,
        objReference, 
        objCustomerName, 
        objCustomerIdentity, 
        objTransactionStatus)
    
    
    print(f'Retorno ListSingleSales: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)