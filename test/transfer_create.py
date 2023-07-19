import json
import sys
import configuration

sys.path.append('/Users/elainecro/Brava/safe2pay')

import safe2pay
from safe2pay.utils import constants
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

def main(arg):
    safe2pay.Safe2Pay(configuration.token_production, '', True, True)

    transfer = safe2pay.Transfer()
    
    bankData = safe2pay.BankData()
    
    bank = safe2pay.Bank()
    bank.Code = "001"
    
    bankData.Bank = bank
    bankData.BankAgency = "7777"
    bankData.AgencyDigit = ""
    bankData.BankAccount = "99977"
    bankData.BankAccountDigit = "9"
    transfer.BankData = bankData
    
    accountType = safe2pay.AccountType()
    accountType.Code = "PP"
    
    transferRegister = safe2pay.TransferRegister()
    transferRegister.BankData = bankData
    
    transferRegister.ReceiverName = "MARIA DA SILVA"
    transferRegister.Amount = 50.10
    transferRegister.Identification = "Mensalidade Julho/2023"
    transferRegister.Identity = "99911177744"
    transferRegister.CompensationDate = "2023-08-10"
    transferRegister.CallbackUrl = "https://callbacks.exemplo.com.br/api/Notify"
    
    transfer.TransferRegisters.add(transferRegister)
    
    response = transfer.PostTransfer()
    print(f'Retorno PostTransfer: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)