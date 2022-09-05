# Texo Award API

Python FastAPI and Sqlalchemy ORM over Postgres database


## Technologies
- Python 3.10
- FastApi - Framework
- Sqlalchemy - ORM
- Docker - Project Structure
- Docker-compose - Development Environment
- SQLite - Development Database
- Alembic - Database migration tool
- PIP - Libraries management tool for Python.


## How to use?

1. Clone this repository
2. Run:
   ``` bash
   make build
   ```
3. Run:
   ``` bash
   make run-server
   ```
4. In your browser call:
  - [API Winners](http://localhost:8000/api/awards/winners/)
  - [Swagger Docs](http://localhost:8000/docs)

#### Testing

To test, just run `make run-test`.
