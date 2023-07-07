# -*- coding: utf-8 -*-
from .lib import *

class Boleto(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.DueDate = DateTime(format="%d/%m/%Y")
		cls.Instruction = String(max=200)
		cls.Message = ObjList(context=cls, key='Message', name='str')
		cls.PenaltyRate = Decimal(max=18,scale=2)
		cls.InterestRate = Decimal(max=18,scale=2)
		cls.CancelAfterDue = Boolean()
		cls.DaysBeforeCancel = Int()
		cls.IsEnablePartialPayment = Boolean()
		cls.DiscountAmount = Decimal(max=18,scale=2)
		cls.DiscountType =  Int()
		cls.DiscountDue = DateTime(format="%d/%m/%Y")


		super().__init__(**kw)
