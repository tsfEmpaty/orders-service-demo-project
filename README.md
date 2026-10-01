<div align="center">

# Orders Service

[![CI](https://github.com/tsfEmpaty/orders-service-demo-project/actions/workflows/ci.yml/badge.svg)](https://github.com/tsfEmpaty/orders-service-demo-project/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-DC382D.svg?logo=redis&logoColor=white)](https://redis.io/)

A demo backend for a mini-store built with **FastAPI**, **PostgreSQL**, **Redis**, and **Alembic**.

</div>

## Overview

This is a learning project focused on building a reliable, production-like backend for a small online store. It includes user registration, product catalog, order management, a fake payment flow, and background notifications.

The project demonstrates three key engineering scenarios:

- **Idempotency** — duplicate requests with the same `Idempotency-Key` do not create double orders or payments.
- **Race-condition safety** — product stock never goes negative, even under concurrent orders.
- **Reliable notifications** — order events are stored in an outbox table and processed by a background worker.

## Tech Stack

- Python 3.13
- FastAPI
- SQLAlchemy 2 (async)
- Alembic
- PostgreSQL
- Redis
- Pydantic Settings
- pytest
- ruff

## Quick Start

```bash
cp .env.example .env
docker compose up --build
```

Check the health endpoint:

```bash
curl http://localhost:8000/health
```

## Project Structure

```
orders-service-demo-project/
├── app/
│   ├── api/            # route handlers
│   ├── core/           # config, security, logging
│   ├── models/         # SQLAlchemy models
│   ├── repositories/   # database access layer
│   ├── services/       # business logic
│   ├── worker/         # background outbox worker
│   └── main.py         # FastAPI entrypoint
├── migrations/         # Alembic migrations
├── tests/              # unit and integration tests
├── locust/             # load tests
├── docker-compose.yml
├── Dockerfile
└── pyproject.toml
```

## Development

Run linters and type checks:

```bash
uv run ruff check .
uvx ty check
```

Run tests:

```bash
uv run pytest
```
