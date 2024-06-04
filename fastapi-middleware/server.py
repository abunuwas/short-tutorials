from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

server = FastAPI()


@server.get("/hello")
def hello():
    return {"message": "hello!"}


@server.middleware("http")
async def check_user_header(request: Request, call_next: RequestResponseEndpoint) -> Response:
    header = request.headers.get("X-User-Type")
    if header is None:
        return JSONResponse(status_code=401, content={"message": "Invalid user type"})
    if header != "cool":
        return JSONResponse(status_code=401, content={"message": "Invalid user type"})
    return await call_next(request)


class CheckUserTypeHeader(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        header = request.headers.get("X-User-Type")
        if header is None:
            return JSONResponse(status_code=401, content={"message": "Invalid user type"})
        if header != "cool":
            return JSONResponse(status_code=401, content={"message": "Invalid user type"})
        return await call_next(request)


server.add_middleware(CheckUserTypeHeader)
