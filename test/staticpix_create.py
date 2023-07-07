import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    pix = safe2pay.StaticPix()
    pix.Ammount = 0.01
    pix.CallbackUrl = "https://callbacks.exemplo.com.br/api/Notify"
    pix.Description = "Este é um pagamento de teste."
    pix.Reference = "Teste QR-Code Estático"

    retorno = pix.CreatePayment()
    print(f'Retorno CreatePayment: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)