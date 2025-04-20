# Python FastAPI Demo Project

## Setup Guide

> You might need to use `python`, `pip` or `python3`, `pip3` based on your machine and installation.

- Ensure that you python3 installed by running `python3 --version`
- Run `python3 -m venv env` to create environment
- Run `source fastapienv/bin/activate` to activate environment
- You can deactivate environment by running `deactivate`
- Run `brew install postgresql` to install postgressql since it is dependency for psycopg2
- Run `pip install -r requirements.txt` to install all the dependecies/packages.

## Running API

- Install `pip install "fastapi[standard]"`
- Run api `uvicorn api.controllers.books:app --reload`
- Run api `fastapi run api/controllers/books.py`
- Run api `fastapi dev api/controllers/books.py`
- Run `uvicorn api.controllers.books:app --reload` to run the application
- Swagger runs on `http://127.0.0.1:8000/docs#/`

## Running tests

- Run `pytest` to run all the tests

# Troubleshooting

## Address already in use

- List the process using port: `lsof -i :<PORT>`
- Terminate process using `sudo kill -9 -<PID>`
