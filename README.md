# Shopping Cart

A simple implementation of a shopping cart using FastAPI.

## How to Install:

1. Download and upgrade pip
    - [python3 -m ensurepip --upgrade](https://pip.pypa.io/en/stable/)
2. Create a virtual environment and activate it
    - [python3 -m venv venv](https://docs.python.org/3/tutorial/venv.html)
    - source venv/bin/activate
2. Install the dependencies:
    - [python3 -m pip install -r requirements/dev.txt](https://pip.pypa.io/en/stable/installing/)

## How to run:
```
make run
# or
python3 -m uvicorn shoppingcart.main:app --reload
```

## Running the tests:
```
make test
# or
python3 -m pytest
```

## Building the container image:
```shell
$ docker build -t shoppingcart .
$ docker run -p 8080:8080 -t -i shoppingcart
```

## Acessing the docs:
After running the app, you can access the docs by visiting the URL: `http://localhost:8000/docs`