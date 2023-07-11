# -*- coding: utf-8 -*-
from .lib import *

class ResponseDetail(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.IdTransaction = Int()
		cls.Status = Int()
		cls.Message = String(max=150)
		cls.Description = String(max=200)
		cls.BankSlipNumber = String(max=50)
		cls.DueDate = DateTime(format="%d/%m/%Y")
		cls.DigitableLine = String(max=50)
		cls.Barcode = String()
		cls.BankSlipUrl = String(max=200)
		cls.OperationDate = DateTime(format="%d/%m/%Y")
		cls.BankName = String(max=100)
		cls.CodeBank = String(max=100)
		cls.Wallet = String(max=100)
		cls.WalletDescription = String(max=200)
		cls.Agency = String(max=30)
		cls.Account = String(max=30)
		cls.CodeAssignor = String(max=30)
		cls.KeyPix = String(max=200)
		cls.QrCodePix = String(max=200)
		cls.AgencyDV = String(max=10)
		cls.AccountDV = String(max=10)
		cls.DocType = String(max=10)
		cls.Accept = String(max=5)
		cls.Currency = String(max=5)
		cls.GuarantorName = String(max=100)
		cls.GuarantorIdentity = String(max=100)

		cls.Id = Int()
		cls.Identifier = String(max=200)
		cls.IdentifierLot = String(max=50)
		cls.QrCode = String(max=150)
		cls.Key = String(max=200)

		cls.Token = String(max=100)
		cls.Tid = String(max=100)
		cls.AuthorizationCode = String(max=100)

		cls.Application = String(max=100)
		cls.Vendor = String(max=100)
		cls.Reference = String(max=100)
		cls.PaymentDate = DateTime(format="%Y-%m-%d")
		cls.PaymentDateTime = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.CreatedDate = DateTime(format="%Y-%m-%d")
		cls.CreatedDateTime = DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.Amount = DecimalS2P(max=18)
		cls.NetValue = DecimalS2P(max=18)
		cls.DiscountAmount = DecimalS2P(max=18)
		cls.TaxValue = DecimalS2P(max=18)
		cls.AmountPayment = DecimalS2P(max=18)

		cls.IsEnabled = Boolean()
		cls.IsProcessed = Boolean()
		cls.InstallmentLimit = Int()
		cls.MinorInstallmentAmmount = Int()
		cls.IsInstallmentEnable = Boolean()
		cls.Customer = Obj(context=cls, key='customer', name='Customer')
		cls.PaymentMethod = String(max=20)#Obj(context=cls, key='paymentmethod', name='PaymentMethod')
		cls.CreditCard = Obj(context=cls, key='creditcard', name='CreditCard')
		cls.Installments = ObjList(context=cls, key='installments', name='Installments')
		cls.Products = ObjList(context=cls, key='products', name='Product')
		cls.CheckingAccounts = ObjList(context=cls, key='checkingaccount', name='CheckingAccount')
		cls.metadata = Dict()

		super().__init__(**kw)
