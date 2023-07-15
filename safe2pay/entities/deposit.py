# -*- coding: utf-8 -*-
from .lib import *

from safe2pay.entities.extract import Extract
from safe2pay.entities.paymentmethod import PaymentMethod

class Deposit(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.id = String(max=26)
		cls.DepositDate = String(max=22)
		cls.Amount = DecimalS2P(max=15)
		cls.Tax = DecimalS2P(max=15)
		cls.IsTransferred = Boolean()
		cls.Message = String(max=200)
		cls.PaymentNumber = String(max=200)
		cls.HashConfirmation = String(max=100)
		cls.Extracts = ObjList(context=cls, key='extracts', name='Extract')
		cls.PaymentMethod = ObjList(context=cls, key='paymentmethod', name='PaymentMethod')
		cls.TotalItems = Int()
		cls.metadata = Dict()

		super().__init__(**kw)
