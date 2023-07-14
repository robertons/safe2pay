import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    singleSale = safe2pay.SingleSale()

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

    singleSale.Customer = customer


    produto = safe2pay.Product()
    produto.Code = '001'
    produto.Description = 'Produto para teste'
    produto.UnitPrice = 100
    produto.Quantity = 1

    singleSale.Products.add(produto)

    paymentMethod1 = safe2pay.PaymentMethod()
    paymentMethod1.CodePaymentMethod = "1" #boleto
    singleSale.PaymentsMethods.add(paymentMethod1)

    paymentMethod2 = safe2pay.PaymentMethod()
    paymentMethod2.CodePaymentMethod = "2" # cartão de crédito
    singleSale.PaymentsMethods.add(paymentMethod2)

    paymentMethod6 = safe2pay.PaymentMethod()
    paymentMethod6.CodePaymentMethod = "6" # pix
    singleSale.PaymentsMethods.add(paymentMethod6)

    singleSale.DueDate = "2023-07-20"
    singleSale.Instruction = "Instrução"
    singleSale.Messages = ["Mensagem 1", "Mensagem 2"]
    singleSale.Reference =  "Referência Sandbox Teste"
    singleSale.PenaltyAmount = "2.00"
    singleSale.InsterestAmount = "10.00"
    singleSale.Emails = [ "elainecro@gmail.com", "email2@teste.com.br"]

    
    split1 = safe2pay.Split()
    split1.CodeTaxType = 2
    split1.CodeReceiverType = "1" #empresa
    #split1.IdReceiver = "Codigo da Empresa no Safe2Pay"
    split1.Identity = "04016399000150"
    split1.Name = "PROVERNETWEB INFORMATICA LTDA"
    split1.IsPayTax = True
    split1.Amount = 30

    singleSale.Splits.add(split1)

    split2 = safe2pay.Split()
    split2.CodeTaxType = 1
    split2.CodeReceiverType = "2" #subconta
    #split2.IdReceiver = "Codigo da Empresa no Safe2Pay"
    split2.Identity = "30239314000102"
    split2.Name = "Subconta 1 Recebedora"
    split2.IsPayTax = True
    split2.Amount = 70

    singleSale.Splits.add(split2)

    # split3 = safe2pay.Split()
    # split3.CodeTaxType = 1
    # split3.CodeReceiverType = "2"
    # #split3.IdReceiver = "Codigo da Empresa no Safe2Pay"
    # split3.Identity = "59303550021"
    # split3.Name = "Subconta 2 Recebedora"
    # split3.IsPayTax = True
    # split3.Amount = 10

    # singleSale.Splits.add(split3)

    singleSale.CallbackUrl = ""

    retorno = singleSale.CreateSingleSale()
    print(f'Retorno CreateSingleSale: {retorno.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)