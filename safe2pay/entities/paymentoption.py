# -*- coding: utf-8 -*-
from .lib import *

class PaymentOption(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.Id = String(max=26)
		cls.Code = String(max=26)
		cls.Name = String(max=26)
		cls.IsEnabled = Boolean()
        #cls.InstallmentLimit = Int()
        #cls.MinorInstallmentAmount = Decimal(max=18,scale=2)
        #cls.IsInstallmentEnable= Boolean()
		cls.PaymentMethod= Obj(context=cls, key='PaymentMethod', name='PaymentMethod')

		super().__init__(**kw)
