# -*- coding: utf-8 -*-
from .lib import *

class Product(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.id = String(max=26)
		cls.CodeTaxType = Int()
		cls.CodeReceiverType = String(max=200)
		cls.IdReceiver = Int()
		cls.Identity = String(max=200)
		cls.Name = String(max=200)
		cls.IsPayTax = Boolean()
		cls.Amount = Decimal(max=18, scale=2)
		cls.metadata = Dict()

		super().__init__(**kw)
