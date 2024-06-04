# FastAPI middleware tutorial
Code for my video tutorial [Create custom middleware with FastAPI](https://youtu.be/P3zdVdb-yn8)

## Run the code

1. Install the dependencies:

```bash
poetry install
```

2. Run the server
```bash
uvicorn server:server --reload 
```

- Check the API docs at http://localhost:8000/docs

- There's only one endpoint: http://localhost:8000/hello

## The project
In this video, I show you how to create middleware in FastAPI using decorator-based and class-based middleware. 
We implement a very simple API, and then we add a simple middleware that checks whether requests have a 
custom header `X-User-Type` and its value. It's best practice to prefix customer headers with `X-` to easily 
tell them apart from standard headers.

## Calling the API with custom headers

When you enable the middleware, your requests will be rejected unless they contain the right header. To add custom
headers to your requests, the easiest way is using curl:

```bash
curl http://localhost:8000/hello -H 'X-User-Type: cool'
```

The `-H` parameter stands for header and adds a header to the request.

## What is FastAPI?
FastAPI is a high-performant REST API framework for Python. 
It's built on top of [Starlette](https://www.starlette.io/) and it uses 
[Pydantic](https://pydantic-docs.helpmanual.io/) for data validation. 
It can generate OpenAPI documentation from your code and also produces a Swagger UI 
that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) 
and give it a star! Also make sure to check out its excellent 
[documentation](https://fastapi.tiangolo.com/) online.

## What is middleware?
Middleware is a layer that pre-processes requests in web servers. Before a request reaches our controllers, 
i.e. the functions that implement endpoints/URLs in our API, there's a pre-processing stage. In that stage, 
the framework parses the request, validates the headers, the content type, the data types, and so on.

Most web development frameworks allow us to create custom middleware, and this is incredibly useful to add 
custom pre-processing components. For example, we may want to check for custom headers in the request. 
We can also use middleware to handle authorization and authentication, to log requests, to implement 
rate-limiting/throttling policies, to track user interactions, and more.

We have two ways of creating custom middleware in FastAPI:

- Decorator-based middleware ([official docs](https://fastapi.tiangolo.com/tutorial/middleware/))

- Class-based middleware ([official docs](https://www.starlette.io/middleware/#basehttpmiddleware))

Decorator-based middleware has a simple and nice interface and it's very convenient for small and simple 
middleware components. Class-based middleware is suitable for complex components that need to be isolated 
and encapsulated into their own modules.

## Want to learn more about API development?

I'm also the author of the following courses and books:

- [Microservice APIs](http://mng.bz/jy4x). Get a 40% discount using the following code: slperalta. Download 2 chapters for free using [this link](https://microapis.io/resources/microservice-apis-in-python).
- [Secure APIs](https://mng.bz/4JVg). This book is currently available in early access, which means only the first few chapters are published and you'll get access to more as I progress in my writing. You also get a chance to give me feedback and help me improve the book. Get a 40% discount using the following code: watchperalta40.
- [Build APIs with Flask](https://www.udemy.com/course/build-apis-with-flask-intro/). FREE.
- [Build APIs with Python: FastAPI Edition](https://learn.microapis.io/p/build-apis-with-fastapi). Get a 30% discount using the following code: 30-OFF-340EF7ED.

Make sure you subscribe to [my newsletter](https://microapis.substack.com/)!