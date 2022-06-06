FROM python:3.8-slim

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc


COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app

EXPOSE 8000:8000

# Run the application
CMD ["uvicorn", "shoppingcart.main:app", "--host", "0.0.0.0", "--port", "8000"]

