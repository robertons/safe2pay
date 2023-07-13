# -*- coding: utf-8 -*-
from .lib import *

class MerchantAccount(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.Identity = String(max=20)
		cls.Name = String(max=150)
		cls.MerchantType = Obj(context=cls, key='MerchantType', name='MerchantType')
		cls.BankData = Obj(context=cls, key='BankData', name='BankData')
		cls.metadata = Dict()

		super().__init__(**kw)
