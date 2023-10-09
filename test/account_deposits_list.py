import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
	# safe2pay.Safe2Pay(configuration.token_production, '', True, True)

	tokenSubconta = '3CBAF4730AD74845B5D6A150E23D15C1'
	safe2pay.Safe2Pay(tokenSubconta, '', True, True)


	transacao = safe2pay.CheckingAccount()
    
	month = "10"
	year = "2023"
	retorno = transacao.ListDeposits(month, year)
    
	print(f'Retorno ListDeposits: {retorno.toJSON()}')


if __name__ == "__main__":
	main(sys.argv)