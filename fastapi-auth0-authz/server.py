from typing import Annotated

import requests
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jws, jwt, ExpiredSignatureError, JWTError, JWSError
from jose.exceptions import JWTClaimsError
from pydantic import BaseModel
from starlette.responses import RedirectResponse

server = FastAPI()


jwks_endpoint = "https://apithreats-test.eu.auth0.com/.well-known/jwks.json"

# https://apithreats-test.eu.auth0.com/.well-known/openid-configuration
# https://accounts.google.com/.well-known/openid-configuration

jwks = requests.get(jwks_endpoint).json()["keys"]


security = HTTPBearer()


def find_public_key(kid):
    for key in jwks:
        if key["kid"] == kid:
            return key


def validate_token(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
):
    try:
        unverified_headers = jws.get_unverified_header(credentials.credentials)
        token_payload = jwt.decode(
            token=credentials.credentials,
            key=find_public_key(unverified_headers["kid"]),
            audience="https://apithreats.com/api/orders",
            algorithms="RS256",
        )
        return UserClaims(
            sub=token_payload["sub"], permissions=token_payload.get("permissions", [])
        )
    except (
        ExpiredSignatureError,
        JWTError,
        JWTClaimsError,
        JWSError,
    ) as error:
        raise HTTPException(status_code=401, detail=str(error))


class UserClaims(BaseModel):
    sub: str
    permissions: list[str]


@server.get("/protected")
def protected(user_claims: UserClaims = Depends(validate_token)):
    return user_claims


@server.get("/login")
def login():
    return RedirectResponse(
        "https://apithreats-test.eu.auth0.com/authorize"
        "?response_type=code"
        "&client_id=<client_id>"
        "&redirect_uri=http://localhost:8000/token"
        "&scope=offline_access openid profile email"
        "&audience=https://apithreats.com/api/orders"
    )


@server.get("/token")
def get_access_token(code: str):
    payload = (
        "grant_type=authorization_code"
        "&client_id=<client_id>"
        "&client_secret=<client_secret>"
        f"&code={code}"
        f"&redirect_uri=http://localhost:8000/token"
    )
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = requests.post(
        "https://apithreats-test.eu.auth0.com/oauth/token", payload, headers=headers
    )
    return response.json()
