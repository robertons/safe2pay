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
    plan.IdMerchant = 1
    plan.PaymentMethod = 2 #cartão de crédito
    plan.PlanOption = 2
    plan.PlanFrequence = 1
    plan.Name = "Teste"
    plan.Description = "Descrição de teste"
    plan.Amount = 10
    #plan.ChargeDay = 10
    plan.SubscriptionTax = 10
    #plan.SubscriptionLimit = 10
    plan.IsProRata = False
    plan.IsImmediateCharge = True,
    plan.BillingCycle = 3
    plan.DaysBeforeChargeDateExpiration = 3
    plan.CallbackUrl = "https://callbacks.exemplo.com.br/api/Notify"
    plan.DaysDue = 20
    plan.DaysBeforeCancel = 10
    plan.Instruction = "Instruções"
    plan.PenaltyAmount = 1
    plan.InterestAmount = 1
    plan.Message = "Mensagem do plano"
    plan.DiscountType = 1
    plan.DiscountDue = "30/07/2023"
    plan.DiscountAmount = 1
    
    plansimulate = safe2pay.PlanSubscription()
    plansimulate.Plan = plan
    plansimulate.SubscriptionDate = "2023-07-20"
    plansimulate.PaymentMethod = 2
    
    response = plansimulate.CreatePlanSimulate()
    
    print(f'Retorno CreatePlanSimulate: {response.toJSON()}')


if __name__ == "__main__":
    main(sys.argv)