import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpaymentdate import MerchantPaymentDate

def main(arg):
	# safe2pay.Safe2Pay(configuration.token_production, '', True, True)
	safe2pay.Safe2Pay('3CBAF4730AD74845B5D6A150E23D15C1', '', True, True)

	merchantPaymentDate = safe2pay.MerchantPaymentDate()
	planFrequence = safe2pay.PlanFrequence()
	planFrequence.Code = "7" # 1 - mensal, 6 semanal, 7 diário
	merchantPaymentDate.PlanFrequence = planFrequence
	#merchantPaymentDate.PaymentDay = 2 # Em caso de frequência semanal, deve ser indicado o dia correspondente da semana, começando pela segunda-feira: 2; até sexta-feira: 6; Caso a frequência for diária, este campo não precisa ser enviado	


	response = merchantPaymentDate.Update()
	print(f'Retorno Update merchantPaymentDate: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)