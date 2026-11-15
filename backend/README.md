# Employee Salary API

FastAPI backend for HR to manage employees, departments and salary history.

## Requirements

- [uv](https://docs.astral.sh/uv/) (installs Python 3.13 automatically)

## Setup

```bash
uv sync
```

## Run (development)

```bash
uv run fastapi dev src/employee_salary_api/main.py
```

- Health check: http://127.0.0.1:8000/health
- API docs: http://127.0.0.1:8000/docs

## Lint & format

```bash
uv run ruff check .
uv run ruff format .
```
