# -*- coding: utf-8 -*-
from .lib import *

class PaymentMethod(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.Id = String(max=26)
		cls.Code = String(max=26)
		cls.CodePaymentMethod = String(max=26)
		cls.Name = String(max=26)
		cls.PaymentMethod = Int()
		cls.IsPayTax = Boolean()
		cls.Taxes = ObjList(context=cls, key='Tax', name='Tax')
		
		super().__init__(**kw)
