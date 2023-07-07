# -*- coding: utf-8 -*-
from .lib import *

class Payment(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Payment'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.Application = String(max=100)
		cls.Vendor = String(max=200)
		cls.CallbackUrl = String(max=200)
		cls.Reference = String(max=60)
		cls.PaymentMethod = String(max=1)
		cls.Meta = Dict()
		cls.ShouldUseAntiFraud = Boolean()
		cls.VisitorID = String(max=40)
		cls.PaymentObject = Obj(context=cls, key='PaymentObject', name='PaymentObject')
		cls.Customer = Obj(context=cls, key='Customer', name='Customer')
		cls.Products = ObjList(context=cls, key='Products', name='Product')
		cls.Splits = ObjList(context=cls, key='Splits', name='Split')
		cls.metadata = Dict()

		super().__init__(**kw)