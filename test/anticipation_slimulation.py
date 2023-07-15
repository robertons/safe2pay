import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    antecipacao = safe2pay.Anticipation()
    antecipacao.PaymentStartDate = '2023-07-01'
    antecipacao.PaymentEndDate = '2023-07-31'

    retorno = antecipacao.Simulate()
    print(f'Retorno Simulate: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)