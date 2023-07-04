# -*- coding: utf-8 -*-
from .lib import *

class Installments(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Payment'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.Installments = Int()
		cls.InstallmentValue= Decimal(max=18, scale=2)
		cls.TotalValue= Decimal(max=18, scale=2)
		cls.AppliedTax = Decimal(max=18, scale=2)

		super().__init__(**kw)
