# -*- coding: utf-8 -*-
from .lib import *

class AccountResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.id = String(max=26)
		cls.InitialDate = DateTime(format="%d/%m/%Y")
		cls.EndDate = DateTime(format="%d/%m/%Y")
		cls.AmountDeposit = DecimalS2P(max=15)
		cls.AmountTax = DecimalS2P(max=15)
		cls.Deposits = ObjList(context=cls, key='Deposits', name='Deposit')
		cls.metadata = Dict()

		super().__init__(**kw)
