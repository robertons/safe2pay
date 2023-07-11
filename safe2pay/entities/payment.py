# -*- coding: utf-8 -*-
from .lib import *
from safe2pay.entities.merchantpayment_response import MerchantPaymentResponse
from safe2pay.entities.paymentobject import PaymentObject

class Payment(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__route__ = '/Payment'
		cls.__typeRoute__ = 'v2'
		
		cls.__metadata__ = {}
		cls.__requireid__ = True

		# FIELDS
		cls.Id = Int()
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

	def CreatePayment(self):
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment
	
	def ChangeDueDateBoleto(self, newDueDate:str):
		paymentObject = PaymentObject()
		paymentObject.Command = '1'
		paymentObject.DueDate = newDueDate

		self.PaymentMethod = '1'
		self.PaymentObject = paymentObject
		
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment
	
	def AddReductionPaymentBoleto(self, discount:decimal):
		paymentObject = PaymentObject()
		paymentObject.Command = '2'
		paymentObject.DiscountPayment = discount

		self.PaymentMethod = '1'
		self.PaymentObject = paymentObject
		
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment
	
	def DelReductionPaymentBoleto(self):
		paymentObject = PaymentObject()
		paymentObject.Command = '3'

		self.PaymentMethod = '1'
		self.PaymentObject = paymentObject
		
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment
	
	def AddDiscountPaymentBoleto(self, discountdue:str, discount:decimal):
		paymentObject = PaymentObject()
		paymentObject.Command = '4'
		paymentObject.DiscountDue = discountdue
		paymentObject.DiscountAmount = discount

		self.PaymentMethod = '1'
		self.PaymentObject = paymentObject
		
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment
	
	def DelDiscountPaymentBoleto(self):
		paymentObject = PaymentObject()
		paymentObject.Command = '5'

		self.PaymentMethod = '1'
		self.PaymentObject = paymentObject
		
		addHeader, route, typeRoute = self.FormatRoute(**{})
		response = Post(f"{route}", self.toJSON(), addHeader, typeRoute)
		payment = MerchantPaymentResponse(**response)
		return payment