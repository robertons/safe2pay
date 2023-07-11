# -*- coding: utf-8 -*-
from .lib import *

class Installments(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Payment'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.Installments = Int()
		cls.InstallmentValue= DecimalS2P(max=18)
		cls.TotalValue= DecimalS2P(max=18)
		cls.AppliedTax = DecimalS2P(max=18)

		super().__init__(**kw)
