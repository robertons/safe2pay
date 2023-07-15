# -*- coding: utf-8 -*-
from .lib import *

    
class MarketplaceObjects(Safe2PayEntity):
	def __init__(cls, **kw):
		cls.__metadata__ = {}
		
		cls.TotalItems = Int()
		cls.Objects = Obj(context=cls, key='MerchantAccount', name='MerchantAccount')
