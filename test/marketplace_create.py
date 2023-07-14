import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_sandbox, '', True, True)

    marketplace = safe2pay.Marketplace()
    marketplace.Name = 'Empresa teste'
    marketplace.CommercialName = 'Serv Tecnologia'
    marketplace.Identity = '30239314000102'
    marketplace.ResponsibleName = 'Nome do Responsável'
    marketplace.ResponsibleIdentity = '53122713063'
    marketplace.ResponsiblePhone = '27999998877'
    marketplace.Email = 'elainecro@gmail.com'
    marketplace.TechName = 'Responsável Técnico'
    marketplace.TechIdentity = '63577242035'
    marketplace.TechEmail = 'elainecro@gmail.com'
    marketplace.TechPhone = '27997562156'

    # bankData
    bankData = safe2pay.BankData()

    bank = safe2pay.Bank()
    bank.Code = '260'
    bankData.Bank = bank

    accountType = safe2pay.AccountType()
    accountType.Code = 'CC'
    bankData.AccountType = accountType

    bankData.BankAgency = '0001'
    bankData.BankAgencyDigit = '0'
    bankData.BankAccount = '1344594'
    bankData.BankAccountDigit = '6'

    marketplace.BankData = bankData

    # address
    address = safe2pay.Address()
    address.ZipCode = '29015380'
    address.Street = 'Rua do Vintém'
    address.Number = '161'
    address.Complement = ''
    address.District = 'Centro'
    address.CityName = 'Vitória'
    address.StateInitials = 'ES'
    address.CountryName = 'Brasil'

    marketplace.Address = address

    # merchantSplit
    tax1 = safe2pay.Tax()
    tax1.TaxTypeName = '2'
    tax1.Tax = 2

    # merchantSplit1 = safe2pay.MerchantSplit()
    # merchantSplit1.PaymentMethodCode = '1'
    # merchantSplit1.IsSubaccountTaxPayer = False
    # merchantSplit1.Taxes.add(tax1)

    merchantSplit2 = safe2pay.MerchantSplit()
    merchantSplit2.PaymentMethodCode = '2'
    merchantSplit2.IsSubaccountTaxPayer = False
    merchantSplit2.Taxes.add(tax1)

    # merchantSplit3 = safe2pay.MerchantSplit()
    # merchantSplit3.PaymentMethodCode = '6'
    # merchantSplit3.IsSubaccountTaxPayer = False
    # merchantSplit3.Taxes.add(tax1)

    # marketplace.MerchantSplit.add(merchantSplit1)
    marketplace.MerchantSplit.add(merchantSplit2)
    # marketplace.MerchantSplit.add(merchantSplit3)

    response = marketplace.CreateSubAccount()
    print(f'Retorno CreateSubAccount: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)