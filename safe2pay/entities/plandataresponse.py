# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.transaction_response import TransactionResponse

class PlanDataResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.idPlan = Int()
		cls.idSubscription = Int()
		cls.subscriptionStatusCode = String(max=20)
		cls.chargeUrl = String(max=100)

		cls.metadata = Dict()

		super().__init__(**kw)