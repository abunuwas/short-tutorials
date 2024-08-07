# FastAPI Docker tutorial
Code for my video tutorial [Run applications in Docker](https://youtu.be/mNpG1zg1QFc)

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

3. Build the image
```bash
docker build -t orders:v1.0.0 . 
```

4. Run the container
```bash
docker run -it -p 8000:8000 orders:v1.0.0 
```

5. Run in the background
```bash
docker run -it -p 8000:8000 -d orders:v1.0.0  
```

6. Check running containers
```bash
docker ps 
```

7. List all containers, running and stopped
```bash
docker ps -a 
```

8. List images
```bash
docker image ls 
```

9. Stop a docker container
```bash
docker stop <container_id> 
```

10. Step inside the container
```bash
docker exec -it <container_id> /bash
```

## The project
In this video, I show you how to dockerize a FastAPI application. We use a very simple FastAPI application
as an example, and go through the process of writing a Dockerfile for the application, building the image,
and running a container off that image.

## What is FastAPI?
FastAPI is a high-performant REST API framework for Python. 
It's built on top of [Starlette](https://www.starlette.io/) and it uses 
[Pydantic](https://pydantic-docs.helpmanual.io/) for data validation. 
It can generate OpenAPI documentation from your code and also produces a Swagger UI 
that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) 
and give it a star! Also make sure to check out its excellent 
[documentation](https://fastapi.tiangolo.com/) online.

## What is Docker?
Docker is a virtualization technology that allows you to build lightweight images. Docker shares the kernel with 
the host machine instead of running its own kernel as traditional virtual machines do. Docker images can be run on 
any platform that has a Docker engine, which allows us to replicate the same environment in production and in local.
The process that runs off a Docker image is called a container.

* Check out the official [Docker docs](https://docs.docker.com/)
* Check out how to install Docker in your platform: [installation guide](https://www.docker.com/)

## Want to learn more about API development?

I'm also the author of the following courses and books:

- [Microservice APIs](http://mng.bz/jy4x). Get a 40% discount using the following code: slperalta. Download 2 chapters for free using [this link](https://microapis.io/resources/microservice-apis-in-python).
- [Secure APIs](https://mng.bz/4JVg). This book is currently available in early access, which means only the first few chapters are published and you'll get access to more as I progress in my writing. You also get a chance to give me feedback and help me improve the book. Get a 40% discount using the following code: watchperalta40.
- [Build APIs with Flask](https://www.udemy.com/course/build-apis-with-flask-intro/). FREE.
- [Build APIs with Python: FastAPI Edition](https://learn.microapis.io/p/build-apis-with-fastapi). Get a 30% discount using the following code: 30-OFF-340EF7ED.

Make sure you subscribe to [my newsletter](https://microapis.substack.com/)!