import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
	#safe2pay.Safe2Pay(configuration.token_production, '', True, True)

	tokenSubconta = '3CBAF4730AD74845B5D6A150E23D15C1'
	safe2pay.Safe2Pay(tokenSubconta, '', True, True)

	conta = safe2pay.CheckingAccount()
    
	initialDate = "2023-08-06"
	endDate = "2023-10-02"
	retorno = conta.GetBalance(initialDate, endDate)
    
	print(f'Retorno GetBalance: {retorno.toJSON()}')
	print(retorno.ResponseDetail[0].AmountAvailableToday)


if __name__ == "__main__":
	main(sys.argv)