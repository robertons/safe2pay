
from safe2pay.utils import constants
import base64
from requests_toolbelt import MultipartEncoder
import requests
import logging
import json
import os
import io
from datetime import datetime
from decimal import Decimal

DEBUG = False
SANDBOX = False
TOKEN = ''
SECRETKEY = ''

def DebugRequest():
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def Safe2Pay(token, secretkey, sandbox=False, debug=False):
    if debug:
        DebugRequest()
    global DEBUG
    global SANDBOX
    global TOKEN
    global SECRETKEY
    DEBUG = debug
    SANDBOX = sandbox
    TOKEN = token
    SECRETKEY = secretkey


def __headers(data=None, addHeader=None, moduleV1=None):
    #hash = base64.b64encode(f'{PRIVATEKEY}:'.encode("utf-8")).decode("utf-8")
    __headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8' if addHeader is None or not 'Content-Type' in addHeader else addHeader['Content-Type'],
        'x-api-key': TOKEN
    }
    if addHeader:
        del addHeader['Content-Type']
        __headers = {**__headers, **addHeader}

    # if SANDBOX:
    #     __headers['IsSandbox'] = True

    return __headers


def __Route(url, typeRoute, module=None):
    switch = {
        'v1': constants.ROUTE_V1,
        'v2': constants.ROUTE_V2_PAYMENT,
        'v2api': constants.ROUTE_V2_API
    }

    urlBase = switch.get(typeRoute)
    if (typeRoute == 'v1'):
        print("URL")
        urlBase = urlBase.replace("{module}", module)
        print(urlBase)
    rota = f'{urlBase}{url}'
    return rota


def Get(url, data={}, addHeader=None, typeRoute=None, module=None):
    return ValidateResponse(requests.get(__Route(url, typeRoute, module), params=data, headers=__headers(data, addHeader)))


def Post(url, data, addHeader=None, typeRoute=None, module=None):
    return ValidateResponse(requests.post(__Route(url, typeRoute, module), json=data, headers=__headers(data, addHeader)))


def Put(url, data, addHeader=None, typeRoute=None, module=None):
    return ValidateResponse(requests.put(__Route(url, typeRoute, module), json=data, headers=__headers(data, addHeader)))


def Patch(url, data, addHeader=None, typeRoute=None, module=None):
    return ValidateResponse(requests.patch(__Route(url, typeRoute, module), json=data, headers=__headers(data, addHeader)))

def Delete(url, addHeader=None, typeRoute=None, module=None):
    return ValidateResponse(requests.delete(__Route(url, typeRoute, module), headers=__headers(None, addHeader)))


def UploadMultiPart(url, files, data=None, addHeader=None, moduleV1=None):
    f = []
    for file in files:
        if isinstance(file, str):
            f.append(('files', (file, open(file, 'rb'))))
        elif isinstance(file, tuple) and isinstance(file[0], str) and (isinstance(file[1], bytes) or isinstance(file[1], io.BufferedReader)):
            f.append(('files', (file[0], file[1])))
    m = MultipartEncoder(fields=f)
    return ValidateResponse(requests.post(__Route(url, moduleV1), data=m, headers=__headers(data, {'Content-Type': m.content_type})))


class Safe2PayException(Exception):
    def __init__(self, message, detail):
        self.message = message
        self.detail = detail

def ValidateResponse(response):

    if response.status_code == 200 or response.status_code == 201:
        try:
            if DEBUG:
                print(f"Response:\n\n {json.dumps(response.json(), indent=4)} \n\n")
            return response.json()
        except:
            if DEBUG:
                print(f"Response:\n\n {response.text} \n\n")
            return response.text
    elif response.status_code > 204:
        status_code = response.status_code
        try:
            response_json = response.json()
            response_json['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response_json['status'] = status_code
            return response.json()
        except Exception as e:
            print("Exceçao: ", e)
            response_json = {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": status_code,
                "message": "Unexpected Error",
                "errors": [
                    {
                        "message": str(e),
                        "errorCode": "0"
                    }
                ]
            }
            return response.text
        #raise Safe2PayException("Safe2Pay Request Error", response_json)

def DecimalToCents(value) -> int:
    return int(value*100)

def CentsToDecimal(value) -> Decimal:
    return Decimal(Decimal(value)/Decimal(100))

def CentsToFloat(value) -> float:
    return float(float(value)/float(100))
