# -*- coding: utf-8 -*-
from .lib import *

class MerchantSplit(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.PaymentMethodCode = String(max=1)
		cls.IsSubaccountTaxPayer = Boolean()
		cls.Taxes = ObjList(context=cls, key='Taxes', name='Tax')
		cls.metadata = Dict()

		super().__init__(**kw)
