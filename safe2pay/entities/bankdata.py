# -*- coding: utf-8 -*-
from .lib import *

class BankData(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.BankAgency = String(max=50)
		cls.BankAgencyDigit = String(max=1)
		cls.BankAccount = String(max=50)
		cls.BankAccountDigit = String(max=1)
		cls.Bank = Obj(context=cls, key='Bank', name='Bank')
		cls.AccountType = Obj(context=cls, key='AccountType', name='AccountType')
		cls.metadata = Dict()

		super().__init__(**kw)
