# -*- coding: utf-8 -*-
from .lib import *

class CheckingAccount(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.Description = String(max=100)
		cls.Amount = DecimalS2P(max=18)
		cls.Tax = DecimalS2P(max=18)
		cls.IsTransferred = Boolean()
		cls.ReleaseDate = DateTime(format="%Y-%m-%d")
		cls.InstallmentNumber = Int()
		cls.metadata = Dict()

		super().__init__(**kw)
