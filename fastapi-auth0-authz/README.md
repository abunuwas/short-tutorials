# Validate JSON Web Tokens (JWTs) issued by Auth0 with FastAPI
Code for my video tutorial [Validate JWTs issued by Auth0 in FastAPI](https://youtu.be/AtmyC945_no)

## Prerequisites

To follow along with this tutorial, you'll need an Auth0 account set up according to the instructions
in [this tutorial](https://youtu.be/PbUcQUQ7K2o). Make sure you go through the whole setup process, since
we'll use all the resources created in that tutorial in this exercise.

This tutorial builds on top of [this previous tutorial](https://youtu.be/ato2S5b27o8) where we set up login and 
learn to issue access tokens with Auth0 and FastAPI. Please make sure you follow this tutorial as well, as the 
current tutorial builds directly on top of that one.

## Set up the environment

1. Copy the `pyproject.toml` and `poetry.lock` files into your machine and install the Python dependencies:

```bash
poetry install
```

2. Activate the virtual environment

```bash
poetry shell
```

## Run the examples

To run the examples, you'll need to replace some values in the code with your own values. This tutorial explains
how to find those values in your Auth0 account, so you can do this while you follow along with the tutorial.

1. In the `server.py` script, replace the following parameters with values from your own Auth0 account:
   - `<authorization_endpoint>` (line 11)
   - `<client_id>` (lines 13 and 24)
   - `<client_secret>` (line 25)
   - `<token_endpoint>` (line 30)

2. Run the machine-to-machine client
```bash
python m2m.py
```

3. Run the authorization code flow implementation:
```bash
uvicorn server:server --reload 
```

- Check the API docs at http://localhost:8000/docs


## The project
In this video, I show you how to integrate FastAPI with Auth0 to log in users and issue API access tokens.

## What is FastAPI?
FastAPI is a high-performant REST API framework for Python. 
It's built on top of [Starlette](https://www.starlette.io/) and it uses 
[Pydantic](https://pydantic-docs.helpmanual.io/) for data validation. 
It can generate OpenAPI documentation from your code and also produces a Swagger UI 
that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) 
and give it a star! Also make sure to check out its excellent 
[documentation](https://fastapi.tiangolo.com/) online.

## What is Auth0?

[Auth0](https://auth0.com/) is one of the most popular identity-as-a-service (IaaS) providers. We use IaaS to handle user management, login,
authorization, and more. These some of the most critical operations in web development, and developers can spend months
stuck on these features. Using an IaaS is a convenient way to manage user login and authorization in a secure and 
scalable way, and it's typically affordable and even free for small projects. Other examples of IaaS are AWS Cognito, 
Firebase, Microsoft Active Directory (now Entra), and FusionAuth.

## Want to learn more about API development?

I'm also the author of the following courses and books:

- [Microservice APIs](http://mng.bz/jy4x). Get a 40% discount using the following code: slperalta. Download 2 chapters for free using [this link](https://microapis.io/resources/microservice-apis-in-python).
- [Secure APIs](https://mng.bz/4JVg). This book is currently available in early access, which means only the first few chapters are published and you'll get access to more as I progress in my writing. You also get a chance to give me feedback and help me improve the book. Get a 40% discount using the following code: watchperalta40.
- [Build APIs with Flask](https://www.udemy.com/course/build-apis-with-flask-intro/). FREE.
- [Build APIs with Python: FastAPI Edition](https://learn.microapis.io/p/build-apis-with-fastapi). Get a 30% discount using the following code: 30-OFF-340EF7ED.

Make sure you subscribe to [my newsletter](https://microapis.substack.com/)!
