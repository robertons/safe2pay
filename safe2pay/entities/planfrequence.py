# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.bankslip_response import BankSlipResponse
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class PlanFrequence(Safe2PayEntity):

	def __init__(cls, **kw):		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.metadata = Dict()
		cls.Code = String(max=1)

		super().__init__(**kw)