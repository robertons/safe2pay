# -*- coding: utf-8 -*-
from .lib import *

class Transaction(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Payment'
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.IdTransaction = String(max=26)
		cls.Status = String(max=26)
		cls.Message = String(max=26)
		cls.Application = String(max=26)
		cls.Vendor = String(max=26)
		cls.Reference = String(max=26)
		cls.PaymentDate = String(max=26)
		cls.PaymentDate = String(max=26)
		cls.CreatedDate = String(max=26)
		cls.CreatedDateTime = String(max=26)
		cls.Amount = String(max=26)
		cls.NetValue = String(max=26)
		cls.DiscountAmount = String(max=26)
		cls.TaxValue = String(max=26)
		cls.PaymentMethod = String(max=26)
		cls.Customer = String(max=26)
		cls.Products = String(max=26)
		cls.AmountPayment = String(max=26)
		cls.CheckingAccounts = String(max=26)
		cls.PaymentObject = String(max=26)
		cls.metadata = Dict()

		super().__init__(**kw)
