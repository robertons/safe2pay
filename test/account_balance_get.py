import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
	#safe2pay.Safe2Pay(configuration.token_production, '', True, True)

	tokenSubconta = '07BFB34E936F4ACEB0BAEB8F3140BFEB'
	safe2pay.Safe2Pay(tokenSubconta, '', True, True)

	conta = safe2pay.CheckingAccount()
    
	initialDate = "2023-07-01"
	endDate = "2023-08-31"
	retorno = conta.GetBalance(initialDate, endDate)
    
	print(f'Retorno GetBalance: {retorno.toJSON()}')


if __name__ == "__main__":
	main(sys.argv)