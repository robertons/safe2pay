import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    transacao = safe2pay.Transaction()

    pageNumber = 1 
    rowsPerPage = 10 
    createdDateInitial = '01/07/2023'
    createdDateEnd = '15/07/2023'
    paymentDateInitial = None
    paymentDateEnd = None
    amountInitial = None
    amountEnd = None
    objId = None
    objReference = None
    objApplication = None
    objVendor = None
    objCustomerName = None
    objCustomerIdentity = None
    objPaymentCode = None
    objTransactionStatus = None
    objIsSandbox = None

    retorno = transacao.GetTransactionList(pageNumber, rowsPerPage, createdDateInitial, createdDateEnd, paymentDateInitial, paymentDateEnd, amountInitial, amountEnd, objId, objReference,objApplication, objVendor, objCustomerName, objCustomerIdentity, objPaymentCode, objTransactionStatus, objIsSandbox)
    
    
    print(f'Retorno GetTransactionList: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)