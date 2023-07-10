import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    transacao = safe2pay.Transaction()
    transacao.Id = 15727456
    transacao.Reference = 'TESTE'
    transacao.CallBackUrl = 'https://callbacks.exemplo.com.br/api/Notify'
    
    transacao.UpdateTransaction(True, True)
    
    print(f'Retorno UpdateTransaction: {transacao.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)