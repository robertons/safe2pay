# -*- coding: utf-8 -*-
from .lib import *

class AccountType(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.Code = String(max=2)
		cls.Name = String(max=150)
		cls.metadata = Dict()

		super().__init__(**kw)
