# -*- coding: utf-8 -*-
from .lib import *

class ResponseDetail(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}		

		# FIELDS
		cls.IdTransaction = Int()
		cls.TransactionID = String(max=100)
		cls.IdTransfer = Int()
		cls.IdTransferRegisterLot = Int()
		cls.IdMerchantRequester = Int()
		cls.Name = String(max=200)
		cls.CommercialName = String(max=200)
		cls.ResponsibleIdentity = String(max=20)
		cls.Email = String(max=100)
		#cls.Emails = ObjList(context=cls, key='Emails', name='str')
		cls.Identity = String(max=20)
		cls.Status = Int() # String(max=50) # - troquei pq tem lugar que retorna string e tem lugar que retorna inteiro
		cls.Message = String(max=150)
		cls.Description = String(max=200)
		cls.BankSlipNumber = String(max=50)
		cls.DueDate = String(max=10) # DateTime(format="%d/%m/%Y") - troquei pq tem lugares que retornam a data em outro formato
		cls.DigitableLine = String(max=50)
		cls.Barcode = String(max=200)
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
		cls.CreatedDate = String(max=22) #DateTime(format="%Y-%m-%d")
		cls.CreatedDateTime = String(max=22) #DateTime(format="%Y-%m-%dT%H:%M:%S")
		cls.Amount = DecimalS2P(max=18)
		cls.NetValue = DecimalS2P(max=18)
		cls.DiscountAmount = DecimalS2P(max=18)
		cls.TaxValue = DecimalS2P(max=18)
		cls.AmountPayment = DecimalS2P(max=18)

		cls.SingleSaleHash = String(max=50)
		cls.SingleSaleUrl = String(max=200)
		cls.CallbackUrl = String(max=200)
		cls.IsApplyPenalty = Boolean()
		cls.PenaltyAmount = DecimalS2P(max=5)
		cls.IsApplyInterest = Boolean()
		cls.InterestAmount = DecimalS2P(max=5)
		cls.Splits = ObjList(context=cls, key='splits', name='Split')


		cls.isCancelled = Boolean()
		cls.IsEnabled = Boolean()
		cls.IsProcessed = Boolean()
		cls.InstallmentLimit = Int()
		cls.MinorInstallmentAmmount = Int()
		cls.IsInstallmentEnable = Boolean()
		cls.Integration = Obj(context=cls, key='integration', name='Integration')
		cls.BankData = Obj(context=cls, key='bankdata', name='BankData')
		cls.Address = Obj(context=cls, key='address', name='Address')
		cls.Customer = Obj(context=cls, key='customer', name='Customer')

		cls.AccountType = Obj(context=cls, key='accounttype', name='AccountType')
		cls.TransferType = Obj(context=cls, key='transfertype', name='AccountType')

		cls.PaymentMethod = String(max=20)#Obj(context=cls, key='paymentmethod', name='PaymentMethod')
		cls.PaymentMethods = ObjList(context=cls, key='paymentmethod', name='PaymentMethod')
		cls.CreditCard = Obj(context=cls, key='creditcard', name='CreditCard')
		cls.Installments = ObjList(context=cls, key='installments', name='Installments')
		cls.Products = ObjList(context=cls, key='products', name='Product')
		cls.CheckingAccounts = ObjList(context=cls, key='checkingaccount', name='CheckingAccount')

		cls.ReceiverName = String(max=150)
		cls.NegotiationTax = DecimalS2P(max=15)
		cls.Identification = String(max=150)
		cls.IsTransferred = Boolean()
		cls.IsReleaseTransfer = Boolean()
		cls.IsNotified = Boolean()
		cls.IsReturned = Boolean()
		cls.IsExcluded = Boolean()
		cls.IsUseCheckingAccount = Boolean()
		cls.HashScheduling = String(max=100)
		cls.HashConfirmation = String(max=100)
		cls.CompensationDate = String(max=22)
		cls.Validation = String(max=100)
	

		cls.AmountReceived = DecimalS2P(max=15)
		cls.AmountPreview = DecimalS2P(max=15)
		cls.AmountCanceled = DecimalS2P(max=15)
		cls.AmountContestation = DecimalS2P(max=15)
		cls.AmountTaxes = DecimalS2P(max=15)
		
		cls.AmountAvailableToday = DecimalS2P(max=15)
		cls.AmountAvailableTotal = DecimalS2P(max=15)
		cls.AmountPreviewTotal = DecimalS2P(max=15)

		cls.Success = Boolean()

		cls.metadata = Dict()

		super().__init__(**kw)
