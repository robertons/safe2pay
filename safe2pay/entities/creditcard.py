# -*- coding: utf-8 -*-
from .lib import *

class CreditCard(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.id = String(max=26)
		cls.Holder = String(max=25)
		cls.CardNumber = String(max=19)
		cls.ExpirationDate = String(max=7)
		cls.SecurityCode = String(max=4)
		cls.Token = String(max=42)
		cls.metadata = Dict()

		super().__init__(**kw)
