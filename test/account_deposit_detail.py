import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
	safe2pay.Safe2Pay(configuration.token_production, '', True, True)

	depositos = safe2pay.CheckingAccount()
    
	day = 13
	month = 7
	year = 2023
	page = 1
	rowsPerPage = 50
	retorno = depositos.DetailDeposits(day, month, year, page, rowsPerPage)
    
	print(f'Retorno DetailDeposits: {retorno.toJSON()}')


if __name__ == "__main__":
	main(sys.argv)