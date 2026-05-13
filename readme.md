# Product Management Microservice

This project is a product management microservice built with **FastAPI**, communicating asynchronously with a **PostgreSQL** database via asyncpg, following a layered architecture.

## 🚀 Features

- **Asynchronous Architecture:** High-performance I/O management with `asyncio`, `asyncpg`, and `FastAPI`.
- **Lifespan Management:** A single database connection pool managed throughout the application lifetime.
- **Layered Architecture:** Modular structure with Router, Service, Repository, and Schema layers.
- **Custom Error Handling:** Application-specific `Exception Handler` structures (404 Not Found, 409 Already Exists).
- **Dependency Injection:** Service and database dependencies managed via FastAPI's DI system.

## 🛠 Technologies Used

- **Backend Framework:** FastAPI
- **Database Driver:** asyncpg (PostgreSQL)
- **Data Validation:** Pydantic (Schemas)
- **Server:** Uvicorn
- **Language:** Python 3.9+

## 📁 Project Structure

```text
postgre-microservices/
├── dependencies/       # Dependency management and DB Pool providers
├── exceptions/         # Custom exception classes
├── repositories/       # Database query layer (CRUD operations)
├── routers/            # API endpoints
├── schemas/            # Pydantic models (Data Validation)
├── services/           # Business logic layer
├── config.py           # Environment variables and configuration
└── main.py             # Application entry point and Lifespan management
```