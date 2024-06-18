# Serverless deployments with FastAPI
Code for my video tutorial [FastAPI serverless deployments on AWS](https://youtu.be/onrNfJ-qZao)

## Prerequisites

To follow along with this tutorial, you'll need:

1. An AWS account
2. A Node.js runtime + npm (installation is platform-dependent, [check here](https://nodejs.org/en/download/package-manager))
3. The AWS CLI. If you wish to make deployments with IAM Identity Center users, you'll need 
   to install the AWS CLI v2. [Check here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) how to install the AWS CLI v2.

The video shows how to make deployments using two strategies:
1. With traditional IAM users
2. With IAM Identity Center users (with temporary credentials)

The video shows you how to set up IAM Identity Center, add users with temporary access, and how 
to configure the AWS CLI to work with temporary credentials.

If you wish to make deployments with traditional IAM users, make sure you create an IAM user, generate 
their access keys, and configure their profile with the AWS CLI.

## Install the serverless framework

Create a folder for the application, and within that folder, run the following commands to install
the serverless framework and the plugins we'll need:

```bash
npm install serverless
npm instll serverless-better-credentials
npm install serverless-python-requirements
```

## Run the code

1. Copy the pyproject.toml file and install the Python dependencies:

```bash
poetry install
```

2. Run the server
```bash
uvicorn server:server --reload 
```

- Check the API docs at http://localhost:8000/docs


## The project
In this video, I show you how to deploy a serverless FastAPI application to AWS.

## What is FastAPI?
FastAPI is a high-performant REST API framework for Python. 
It's built on top of [Starlette](https://www.starlette.io/) and it uses 
[Pydantic](https://pydantic-docs.helpmanual.io/) for data validation. 
It can generate OpenAPI documentation from your code and also produces a Swagger UI 
that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) 
and give it a star! Also make sure to check out its excellent 
[documentation](https://fastapi.tiangolo.com/) online.

## Want to learn more about API development?

I'm also the author of the following courses and books:

- [Microservice APIs](http://mng.bz/jy4x). Get a 40% discount using the following code: slperalta. Download 2 chapters for free using [this link](https://microapis.io/resources/microservice-apis-in-python).
- [Secure APIs](https://mng.bz/4JVg). This book is currently available in early access, which means only the first few chapters are published and you'll get access to more as I progress in my writing. You also get a chance to give me feedback and help me improve the book. Get a 40% discount using the following code: watchperalta40.
- [Build APIs with Flask](https://www.udemy.com/course/build-apis-with-flask-intro/). FREE.
- [Build APIs with Python: FastAPI Edition](https://learn.microapis.io/p/build-apis-with-fastapi). Get a 30% discount using the following code: 30-OFF-340EF7ED.

Make sure you subscribe to [my newsletter](https://microapis.substack.com/)!
