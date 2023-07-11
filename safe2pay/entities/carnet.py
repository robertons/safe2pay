# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse

class Carnet(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Carnet'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.id = String(max=26)
		cls.IsSandbox = Boolean()
		cls.Application = String(max=100)
		cls.Vendor = String(max=200)
		cls.CallbackUrl = String(max=200)
		cls.PaymentMethod = Int()
		cls.Reference = String(max=60)
		cls.Customer = Obj(context=cls, key='customer', name='Customer')
		cls.Products = ObjList(context=cls, key='Products', name='Product')
		cls.PaymentObject = Obj(context=cls, key='PaymentObject', name='PaymentObject')
		cls.BankSlips = ObjList(context=cls, key='BankSlip', name='BankSlip')
		cls.Splits = ObjList(context=cls, key='Splits', name='Split')
		
		cls.metadata = Dict()

		super().__init__(**kw)
