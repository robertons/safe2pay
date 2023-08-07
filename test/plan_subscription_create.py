import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    plan = safe2pay.Plan()
    plan.PaymentMethod = 2 #cartão de crédito
    
    plan.Emails = ['elainecro@gmail.com']
    
    customer = safe2pay.Customer()
    customer.Name = "Elaine Cristina Assinante"
    customer.Identity = "10808807714"
    customer.Email = 'elaine@optsol.com.br'
    
    address = safe2pay.Address()
    address.Street = "Rua de Teste"
    address.Number = "12"
    address.District = "Vitória"
    address.ZipCode = "29015000"
    address.Complement = "Complemento"
    
    city = safe2pay.City()
    city.CodeIBGE = "3205309"
    address.City = city
    customer.Address = address
    
    plan.Customer = customer
    plan.Token = "36f676af6df14d16b2132230ecd2e5d8"

    
    response = plan.CreateSubscription("10623")
    print(f'Retorno CreateSubscription: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)