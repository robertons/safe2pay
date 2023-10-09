# -*- coding: utf-8 -*-
from .lib import *

class CustomerTransactionResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.id = String(max=26)
		cls.Name = String(max=200)
		cls.Email = String(max=150)
		cls.Phone = String(max=150)
		cls.Identity = String(max=14)
		cls.Address = Obj(context=cls, key='address', name='AddressTransactionResponse')
		cls.metadata = Dict()

		super().__init__(**kw)
