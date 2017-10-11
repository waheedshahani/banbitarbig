import requests
import json
import hmac
import time
import hashlib
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode
#client_key = 'HR17YPXP-1V0YV1O2-063BA47D-BLMDXFFN-RO2H0K2Z'
#client_secret = b'5f8a863537d4c1e0a27d192bc22369ae88f29b833a4ab8d351e07dee1caa7d90'


class bancor:
	url='https://api.bancor.network/0.1/currencies/594bb7e468a95e00203b048d/rate?targetCurrencyId=5937d635231e97001f744267'
	def publicAPICall(self):
		return json.loads(requests.get(self.url).text)
	def getTicker(self):
		return self.publicAPICall()
