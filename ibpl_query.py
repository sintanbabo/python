import requests
from requests import auth
import json

tenantId = '5814'
token = 'uztr2uvf.udk74cvyksfkewfvuejc2a8'

service_url = f"https://mygcppmm.o9solutions.com/api/ibplquery/{tenantId}/ExecuteQueryJson"

headers = {"Authorization": f"ApiKey {token}"}

data = {
    "Query": "SELECT ([Item].[Item]) limit 1;"
}

try:
    # 10초 동안 기다린 후 타임아웃
    res = requests.post(service_url, json=data, headers=headers, timeout=60)
    print(res.status_code)
    print(res.json())
except requests.exceptions.Timeout as e:
    print("Timeout Error : ", e)
except requests.exceptions.ConnectionError as e:
    print(f"ConnectionError : {e}")
except requests.exceptions.HTTPError as e:
    print(f"HTTPError : {e}")
except requests.exceptions.RequestException as e:
    print(f"RequestException : {e}")
except requests.exceptions.TooManyRedirects as e:
    print(f"TooManyRedirects : {e}")