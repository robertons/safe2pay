# -*- coding: utf-8 -*-

from .datatype import *
from safe2pay.utils.safe2pay import *
from datetime import datetime
import re

__methods__ = ['toJSON', 'FormatRoute', 'load', 'add', 'Create', 'Update', 'Get', 'List',
               'Delete','ReleaseBankSlip', 'ListMerchantPayment', 'GetInstallmentValues',
               'CreatePayment','ChangeDueDateBoleto', 'AddReductionPaymentBoleto', 
               'DelReductionPaymentBoleto','AddDiscountPaymentBoleto','DelDiscountPaymentBoleto',
               'WriteOffBankSlip', 'CancelPix', 'CancelCredit', 'CaptureCredit', 'UpdateTransaction',
               'UpdateSandboxTransaction','GetTransaction','GetTransactionByReference', 
               'GetTransactionList', 'GetCarneta', 'ResendCarneta', 'CancelCarneta', 'CreateToken',
               'DeleteToken', 'CreateSubAccount', 'GetSubAccount', 'GetList', 'PutSubAccount', 
               'DeleteSubAccount','CreateSingleSale','CancelSingleSale','ListSingleSales',
               'GetSingleSale','ResendSingleSale','ListDeposits', 'DetailDeposits','GetMerchantBankData',
               'GetBalance', 'Simulate', 'EffectSimulate','PostTransfer', 'GetTransfer', 'ListTransfers',
               'ListLotTransfers', 'CreatePlan','GetPlan','ListPlans','DisablePlan', 'CreateSubscription',
               'CreatePlanSimulate','GetSubscription','ListSubscriptions','GetSubscriptionCharges',
               'DisableSubscription','UpdateTokenCard','ListChargebacks','GetChargeback','ListPaymentMethods',
               'GetPaymentMethod']


def EncodeValue(o, format=None):
    try:
        if hasattr(o, 'toJSON'):
            return o.toJSON()
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, datetime):
            return o.strftime(format) if format != 'iso' else o.isoformat()
        if isinstance(o, bytes):
            return o.decode('utf-8')
        return o
    except Exception as e:
        raise e


class Safe2PayEntity():

    def __init__(self, aliases=None, context=None, **kw):
        self.__metadata__['data'] = {}
        self.__metadata__['relasionships'] = {}
        self.__context__ = context
        self.load(**kw)

    def load(self, **kw):
        if len(kw) > 0:
            for k in self.__dict__:
                try:
                    if not k.startswith("__"):
                        if k in kw:
                            #if (self[k].value != None):
                            if self[k].__class__.__name__.startswith("Obj"):
                                self.add(k, kw[k])
                            else:
                                self[k].value = kw[k]
                                self.__metadata__['data'][k] = EncodeValue(self[k].value, self[k].format)
                except Exception as e:
                    raise Exception(f"[{self.__class__.__name__}] Field [{k}] Value [{kw[k]}] Error : {e}")

    def add(self, key=None, data=None):
        if key and (isinstance(data, dict) or isinstance(data, list)):
            if "List" in self[key].__class__.__name__:
                if not key in self.__metadata__['relasionships']:
                    self.__metadata__['relasionships'][key] = []
                self.__metadata__['relasionships'][key].extend(
                    data if isinstance(data, list) else [data])

                if hasattr(data, 'values'):

                    self[key].value.extend([self[key].type(context={'entity': self, 'key': key}, **item) for item in data if any(item.values(
                    ))] if isinstance(data, list) else [self[key].type(context={'entity': self, 'key': key}, **data)] if any(data.values()) else [])

                elif isinstance(data, list):
                    self[key].value.extend([self[key].type(item) if isinstance(item, str) or isinstance(
                        item, int) else self[key].type(context={'entity': self, 'key': key}, **item) for item in data if not item is None])
            else:
                data = data[0] if isinstance(data, list) else data
                if any(data.values()):
                    self.__metadata__['relasionships'][key] = data
                    self[key].value = self[key].type(context={'entity': self, 'key': key}, **data)
        elif hasattr(data, '__class__') and data.__class__.__name__ == self[key].type.__name__:
            self.__setattr__(key, data)
        else:
            raise Exception(f"[{self.__class__.__name__}] entity.add requires key and dict of object data")

    def __getitem__(self, field):
        return super().__getattribute__(field) if hasattr(self, field) else None

    def __getattribute__(self, field):
        if field.startswith("__") or field in __methods__:
            return super().__getattribute__(field)
        else:
            return super().__getattribute__(field).value

    def __setattr__(self, item, value):
        try:
            if not item.startswith("__") and not "entity.datatype" in str(value.__class__):
                if self[item]:
                    if hasattr(value, '__context__') and not value.__context__:
                        value.__context__ = self
                    self[item].value = value
                    self.__metadata__['data'][item] = EncodeValue(self[item].value, self[item].format)

                    if 'type' in self[item].__dict__ and self[item].__dict__ ['type']:
                        if not 'list' in self[item].__class__.__name__:
                            self[item].__dict__['context'].__metadata__['relasionships'][item] = EncodeValue(self[item].value, self[item].format)

                    if self.__context__:
                        _context = self.__context__['entity']
                        _context_key = self.__context__['key']
                        if isinstance(_context[_context_key].value, list):
                            index = _context[_context_key].value.index(self)
                            _context.__metadata__[
                                'relasionships'][_context_key][index] = self.__metadata__['data']
                        else:
                            _context.__metadata__[
                                'relasionships'][_context_key] = self.__metadata__['data']


                else:
                    super().__setattr__(item, value)
            else:
                super().__setattr__(item, value)
        except Exception as e:
            raise Exception(f"[{self.__class__.__name__}] Field [{item}] Value [{value}] Error : {e}")

    def toJSON(self):
        try:
            return {**self.__metadata__['data'], **self.__metadata__['relasionships']}
        except Exception as e:
            raise e

    def  FormatRoute(self, **kw):
        _header = None
        _route = self.__route__
        _typeRoute = self.__typeRoute__

        if 'resourceToken' in kw:
            _header = {'resourceToken' :kw['resourceToken']}

        result = re.findall(r"\{(\w+)\}", _route)
        if result:
            for param in result:
                if not param in kw:
                    raise Exception(f"[{self.__class__.__name__}] Param ({param}) is required on method")
            _route = _route.format(**kw)

        if hasattr(self, '__identifier__'):
            if not self.__identifier__ in kw:
                raise Exception(f"[{self.__class__.__name__}] Param ({self.__identifier__}) is required on params")
            route = f"{route}?{self.__identifier__}={kw[self.__identifier__]}"

        return _header, _route, _typeRoute

    def Create(self, **kw):
        if hasattr(self, '__route__'):
            addHeader, route, typeRoute = self.FormatRoute(**kw)
            data = Post(route, self.toJSON(), addHeader, typeRoute)
            self.load(**data)
        else:
            raise Exception(f"[{self.__class__.__name__}] Method Create not allowed this object")
        return self

    def Update(self, **kw):
        if hasattr(self, '__route__'):
            addHeader, route, typeRoute = self.FormatRoute(**kw)
            data = Put(route, self.toJSON(), addHeader, typeRoute)
            self.load(**data)
        else:
            raise Exception(f"[{self.__class__.__name__}] Method Update not allowed this object")
        return self

    def Get(self, **kw):
        if hasattr(self, '__route__'):
            addHeader, route, typeRoute = self.FormatRoute(**kw)
            response = Get(route, addHeader, typeRoute)
            self.load(**response)
        else:
            raise Exception(f"[{self.__class__.__name__}] Method Get not allowed this object")
        return self

    def List(self, filters=None, **kw):
        if hasattr(self, '__route__'):
            addHeader, route, typeRoute = self.FormatRoute(**kw)
            qs =''
            if filters:
                qs = '?' + '&'.join([f'{k}={v}' for k,v in filters.items()])
            route = f"{route}{qs}"
            response = Get(route, addHeader, typeRoute)
            _class = getattr(__import__(f'{self.__module__}', fromlist=[self.__class__.__name__]), self.__class__.__name__)
            return ListType(_class).add([_class(**item) for item in response['data']]) if 'data' in response else ListType(_class)
        else:
            raise Exception(f"[{self.__class__.__name__}] Method Get not allowed this object")
        return self

    def Delete(self, **kw):
        if hasattr(self, '__route__'):
            addHeader, route, typeRoute = self.FormatRoute(True, **kw)
            Delete(route, addHeader, typeRoute)
        else:
            raise Exception(f"[{self.__class__.__name__}] Method Delete not allowed this object")
        self = None
        return None
