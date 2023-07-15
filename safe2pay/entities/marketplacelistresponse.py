# -*- coding: utf-8 -*-
from .lib import *

from safe2pay.entities.marketplaceobjects import MarketplaceObjects

class MarketplaceListResponse(Safe2PayEntity):

	def __init__(cls, **kw):

		cls.__metadata__ = {}

		# FIELDS
		cls.id = String(max=26)
		cls.HasError = Boolean()
		cls.Error = String(max=150)
		cls.ErrorCode = String(max=10)
		cls.ResponseDetail = Obj(context=cls, key='MarketplaceObjects', name='MarketplaceListResponse')
		cls.metadata = Dict()

		super().__init__(**kw)