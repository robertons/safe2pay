# -*- coding: utf-8 -*-
from .lib import *

class Split(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.id = String(max=26)
		cls.CodeTaxType = Int()
		cls.CodeReceiverType = String(max=1)
		cls.IdReceiver = Int()
		cls.Identity = String(max=14)
		cls.Name = String(max=100)
		cls.IsPayTax = Boolean()
		cls.Amount = DecimalS2P(max=18)
		cls.metadata = Dict()

		super().__init__(**kw)
