import requests

endpoint = 'https://httpbin.org'

endpoint_200 = 'https://httpbin.org/#/HTTP_Methods/get_get'

get_response = requests.get(endpoint_200)
print(get_response.text)
