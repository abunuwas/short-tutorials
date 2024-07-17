import requests
from fastapi import FastAPI
from starlette.responses import RedirectResponse

server = FastAPI()


@server.get("/login")
def register():
    return RedirectResponse(
        "<authorization_endpoint>"
        "?response_type=code"
        "&client_id=<client_id>"
        "&redirect_uri=http://localhost:8000/token"
        "&scope=offline_access openid profile email"
        "&audience=https://microapis.io/api/orders"
    )


@server.get("/token")
def get_access_token(code: str):
    payload = (
        "grant_type=authorization_code"
        "&client_id=<client_id>"
        f"&client_secret=<client_secret>"
        f"&code={code}"
        f"&redirect_uri=http://localhost:8000/token"
    )
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = requests.post("<token_endpoint>", payload, headers=headers)
    return response.json()
