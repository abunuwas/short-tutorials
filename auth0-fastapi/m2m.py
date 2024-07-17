import requests

payload = {
    "client_id": "<client_id>",
    "client_secret": "<client_secret>",
    "audience": "https://microapis.io/api/orders",
    "grant_type": "client_credentials",
}

response = requests.post(
    "https://microapis-test.eu.auth0.com/oauth/token", json=payload
)

print(response.json())
