# Deploy with Render.com tutorial
Code for my video tutorial [Deploy with Render.com tutorial](https://youtu.be/nOP8khZhjhk)

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


## The project
In this video, I show you how to deploy a simple FastAPI application to Render.com. The application represents a 
very simple orders API with a small database. When running locally, the database is a SQLite database, while on 
Render.com we connect the application to a PostgreSQL database.

## What is FastAPI?
FastAPI is a high-performant REST API framework for Python. 
It's built on top of [Starlette](https://www.starlette.io/) and it uses 
[Pydantic](https://pydantic-docs.helpmanual.io/) for data validation. 
It can generate OpenAPI documentation from your code and also produces a Swagger UI 
that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) 
and give it a star! Also make sure to check out its excellent 
[documentation](https://fastapi.tiangolo.com/) online.

## What Render.com?
Render is a fully managed cloud platform. To make deployments to Render, you connect your GitHub repository to a 
Render application, and on every push to the main branch, it auto-deploys. Simply provide configuration for how to 
build and run the application, and create a database if needed. In this tutorial, we go through all those steps.

## Want to learn more about API development?

I'm also the author of the following courses and books:

- [Microservice APIs](http://mng.bz/jy4x). Get a 40% discount using the following code: slperalta. Download 2 chapters for free using [this link](https://microapis.io/resources/microservice-apis-in-python).
- [Secure APIs](https://mng.bz/4JVg). This book is currently available in early access, which means only the first few chapters are published and you'll get access to more as I progress in my writing. You also get a chance to give me feedback and help me improve the book. Get a 40% discount using the following code: watchperalta40.
- [Build APIs with Flask](https://www.udemy.com/course/build-apis-with-flask-intro/). FREE.
- [Build APIs with Python: FastAPI Edition](https://learn.microapis.io/p/build-apis-with-fastapi). Get a 30% discount using the following code: 30-OFF-340EF7ED.

Make sure you subscribe to [my newsletter](https://microapis.substack.com/)!
