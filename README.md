# VIS4ML Service

Visualization for Machine Learning

## Features

Environment configuration example

## Quick Start

### Prerequisites

- Python 3.12 or higher
- pip or uv package manager

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd vis4ml-service
```

2. Create a virtual environment:

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
uv venv
source .venv/bin/activate
```

Install dependencies:

```bash
uv pip install -e .
# or for development:
uv pip install -e ".[dev]"
```

4. Create a `.env` file (copy from `.env.example`):

```bash
cp .env.example .env
```

### Running the Application

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# or development mode with auto-reload:
uv run python main.py
```

The API will be available at:

- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

## API Endpoints

### Health Check

- `GET /health` - Application health status

### Data Domain

- `GET /api/v1/data/hello` - Hello world from data API

### Model Domain

- `GET /api/v1/model/hello` - Hello world from model API

## Development

### Running Tests

```bash
# run all tests:
uv run pytest

# run with coverage:
uv run pytest --cov=app --cov-report=html

# run specific test file:
uv run pytest tests/domains/test_data_api.py
```

### Code Quality

Format code with ruff:

```bash
ruff check --fix .
ruff format .
```

## Architecture Highlights

### Dynamic Domain Loading

### Request Correlation

Every request is assigned a unique correlation ID for tracing across logs and responses. The ID is returned in the `X-Correlation-ID` header.

### Error Handling

All errors follow a consistent format:

```json
{
  "error_code": "NOT_FOUND",
  "message": "Resource not found",
  "details": {},
  "correlation_id": "uuid-here"
}
```

### Middleware Stack

1. CORS middleware (configurable origins)
2. Request logging middleware (correlation IDs, timing)
