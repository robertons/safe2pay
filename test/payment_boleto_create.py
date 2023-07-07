import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    paymentObject = safe2pay.PaymentObject()
    paymentObject.DueDate = '10/07/2023'
    paymentObject.Instruction = 'Instrução de exemplo'
    paymentObject.Message = ['Mensagem 1', 'Mensagem 2', 'Mensagem 3']
    paymentObject.PenaltyRate = 2.25
    paymentObject.InterestRate = 1.23
    paymentObject.CancelAfterDue = True
    #paymentObject.DaysBeforeCancel = 2
    paymentObject.IsEnablePartialPayment = False
    paymentObject.DiscountAmount = 0.01
    paymentObject.DiscountType = 1
    paymentObject.DiscountDue = '09/07/2023'

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
    customer.Identity = '10808807714'
    customer.Email = 'elainecro@gmail.com'
    customer.Phone = '27997562156'
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

    boleto = safe2pay.Payment()
    boleto.Application = configuration.application
    boleto.Vendor = "Elaine Cristina - Vendedor Teste"
    boleto.CallbackUrl = ""
    boleto.Reference = "REF_TESTE_BOLETO"
    boleto.PaymentMethod = constants.PAYMENT_BOLETO
    boleto.PaymentObject = paymentObject
    boleto.Customer = customer
    boleto.Products.add(produto)
    #boleto.Splits.add(split1)
    #boleto.Splits.add(split2)
    #boleto.Splits.add(split3)

    retorno = boleto.CreatePayment()
    print(f'Retorno CreatePayment: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)