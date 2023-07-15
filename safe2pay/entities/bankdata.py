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
		cls.Agency = String(max=50)
		cls.AgencyDigit = String(max=10)
		cls.Account = String(max=30)
		cls.AccountDigit = String(max=10)
		cls.Operation = String(max=50)
		cls.AccountType = Obj(context=cls, key='AccountType', name='AccountType')
		cls.Metadata = Dict()

		super().__init__(**kw)
