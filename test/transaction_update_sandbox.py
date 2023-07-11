import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_sandbox, '', True, True)

    transacao = safe2pay.Transaction()

    transacao.UpdateSandboxTransaction(58187161, 3)
    
    print(f'Retorno UpdateSandboxTransaction: {transacao.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)