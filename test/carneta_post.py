import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_sandbox, '', True, True)

    paymentObject = safe2pay.PaymentObject()
    paymentObject.PenaltyAmount = 10
    paymentObject.InterestAmount = 5

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

    bankSlip1 = safe2pay.BankSlip()
    bankSlip1.Amount = 10
    bankSlip1.DueDate = '15/07/2023'
    bankSlip1.Message = ['Mensagem1', 'Mensagem2', 'Mensagem3']
    bankSlip1.DiscountAmount = 1
    bankSlip1.DiscountType = 1 # 1 = valor fixo até o vencimento. 2 = valor por antecipação em dias corridos. 3 = valor por antecipação em dias úteis..
    bankSlip1.DiscountDue = '14/07/2023'

    bankSlip2 = safe2pay.BankSlip()
    bankSlip2.Amount = 10
    bankSlip2.DueDate = '15/08/2023'
    bankSlip2.Message = ['Mensagem1', 'Mensagem2', 'Mensagem3']
    bankSlip2.DiscountAmount = 1
    bankSlip2.DiscountType = 1 # 1 = valor fixo até o vencimento. 2 = valor por antecipação em dias corridos. 3 = valor por antecipação em dias úteis..
    bankSlip2.DiscountDue = '14/08/2023'

    carne = safe2pay.Carnet()
    #carne.IsSandbox = True
    carne.Application = configuration.application
    carne.Vendor = "Elaine Cristina - Vendedor Teste"
    carne.CallbackUrl = ""
    carne.Reference = "REF_TESTE_carne"
    carne.PaymentMethod = constants.PAYMENT_BOLETO
    carne.Customer = customer
    carne.Products.add(produto)
    carne.PaymentObject = paymentObject
    carne.BankSlips.add(bankSlip1)
    carne.BankSlips.add(bankSlip2)
    #carne.Splits.add(split1)
    #carne.Splits.add(split2)
    #carne.Splits.add(split3)

    retorno = carne.Create()
    print(f'Retorno Create: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)