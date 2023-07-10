import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    paymentObject = safe2pay.PaymentObject()
    paymentObject.InstallmentQuantity = 1
    paymentObject.IsPreAuthorization = False
    paymentObject.IsApplyInterest = False
    # paymentObject.InterestRate = 0

    # Informe esse grupo caso o cartão de crédito não esteja tokenizado
    paymentObject.Holder = "ELAINE C R OLIVEIRA"
    paymentObject.CardNumber = "0000000000000000"
    paymentObject.ExpirationDate = "03/2030"
    paymentObject.SecurityCode = "737"

    # Informe esse grupo caso o cartão de crédito já esteja tokenizado
    #paymentObject.Token = "tokenGerado"

    addrCustomer = safe2pay.Address()
    addrCustomer.ZipCode = '29015330'
    addrCustomer.Street = 'Rua Graciano Neves'
    addrCustomer.Number = '99'
    addrCustomer.Complement = 'ed. Antares'
    addrCustomer.District = 'Centro'
    addrCustomer.StateInitials = 'ES'
    addrCustomer.CityName = 'Vitória'
    addrCustomer.CountryName = 'Brasil'

    customer = safe2pay.Customer()
    customer.Name = 'Elaine Cristina Compradora'
    customer.Identity = '40515047007'
    customer.Email = 'teste@gmail.com'
    customer.Phone = '27997569999'
    customer.Address = addrCustomer

    produto = safe2pay.Product()
    produto.Code = '001'
    produto.Description = 'Produto para teste'
    produto.UnitPrice = 1
    produto.Quantity = 1

    split1 = safe2pay.Split()
    split1.CodeTaxType = 1
    split1.CodeReceiverType = "1"
    #split1.IdReceiver = "Codigo da Empresa no Safe2Pay"
    split1.Identity = "27214511000162"
    split1.Name = "Empresa Recebedora"
    split1.IsPayTax = True
    split1.Amount = 20

    split2 = safe2pay.Split()
    split2.CodeTaxType = 1
    split2.CodeReceiverType = "2"
    #split2.IdReceiver = "Codigo da Empresa no Safe2Pay"
    split2.Identity = "44447716070"
    split2.Name = "Subconta 1 Recebedora"
    split2.IsPayTax = True
    split2.Amount = 70

    split3 = safe2pay.Split()
    split3.CodeTaxType = 1
    split3.CodeReceiverType = "2"
    #split3.IdReceiver = "Codigo da Empresa no Safe2Pay"
    split3.Identity = "59303550021"
    split3.Name = "Subconta 2 Recebedora"
    split3.IsPayTax = True
    split3.Amount = 10

    cartao = safe2pay.Payment()
    cartao.Application = configuration.application
    cartao.Vendor = "Elaine Cristina - Vendedor Teste"
    cartao.CallbackUrl = ""
    cartao.Reference = "REF_TESTE_cartao"
    cartao.PaymentMethod = constants.PAYMENT_CARTAO
    cartao.ShouldUseAntiFraud = False
    cartao.VisitorID = ""
    cartao.PaymentObject = paymentObject
    cartao.Customer = customer
    cartao.Products.add(produto)
    #cartao.Splits.add(split1)
    #cartao.Splits.add(split2)
    #cartao.Splits.add(split3)

    retorno = cartao.CreatePayment()
    print(f'Retorno CreatePayment: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)