# Shopping Cart

A simple implementation of a shopping cart using FastAPI.

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