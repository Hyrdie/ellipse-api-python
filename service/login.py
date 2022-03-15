from typing import Optional
from suds.client import Client
from suds.wsse import *

def login(username: str, password: str, position: str, district: str):
    security = Security()
    token = UsernameToken(username, password)
    security.tokens.append(token)
    url = 'http://ellipse-demo.ems-elltst.ems.co.id/ews/services/AuthenticatorService?WSDL'
    client = Client(url)
    client.set_options(wsse=security)
    post_authenticate = client.factory.create('OperationContext')
    # post_authenticate.position = "ST OPS"
    # post_authenticate.district = "SERV"
    post_authenticate.position = position
    post_authenticate.district = district
    post_authenticate.maxInstances = 100
    try:
        authenticate = client.service.authenticate(post_authenticate)
        return authenticate, post_authenticate.position, post_authenticate.district
    except Exception as e:
        return str(e)