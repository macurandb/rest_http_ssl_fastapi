# REST HTTP SSL FastAPI Example Project

This project demonstrates how to set up a FastAPI application with SSL support and write tests using `httpx` and `pytest-asyncio`. The project is managed using [Poetry](https://python-poetry.org/), a tool for dependency management and packaging in Python.

## Table of Contents

- [Installation](#installation)
- [Running the Server](#running-the-server)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [License](#license)

## Installation

To get started with this project, follow these steps:

1. **Install Poetry**: If you don't have Poetry installed, you can install it by running:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/rest_http_ssl_fastapi.git
    cd rest_http_ssl_fastapi
    ```

3. **Install dependencies**: Once inside the project directory, install the required dependencies using Poetry:

    ```bash
    poetry install
    ```

## Running the Server

To run the FastAPI server with SSL enabled, ensure you have your SSL certificates ready:

1. **Place your SSL certificates**: Make sure you have `cert.pem` and `key.pem` files located in the `certs/` directory. If you need to generate self-signed certificates for testing, you can use the following commands:

    ```bash
    mkdir certs
    openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -days 365 -nodes
    ```

2. **Start the server**: Run the FastAPI application using Poetry:

    ```bash
    poetry run python src/restapi/main.py
    ```

    The server will be accessible at `https://localhost:8000/`.

## Testing

The project includes tests that can be executed without running the FastAPI application as a separate service.

1. **Run the tests**: Execute the tests using the following command:

    ```bash
    poetry run pytest
    ```

    These tests are located in the `tests/restapi/` directory and are designed to ensure that the API endpoints behave as expected.

## Project Structure

Below is an overview of the project's directory structure:

```plaintext
fastapi-ssl-example/
├── certs/                      # Directory containing SSL certificates
│   ├── cert.pem
│   └── key.pem
├── src/
│   └── restapi/
│       ├── main.py             # Main FastAPI application
│       └── __init__.py
├── tests/
│   └── restapi/
│       ├── test_main.py        # Test file for the FastAPI application
│       └── __init__.py
├── pyproject.toml              # Poetry configuration file
└── README.md                   # Project README file
```

## Configuration

### SSL Certificates

- **cert.pem**: The public certificate for SSL.
- **key.pem**: The private key for SSL.

These files must be present in the `certs/` directory. You can change the paths in the `main.py` file if your certificates are stored elsewhere.

### Testing Configuration

The testing setup uses `httpx.AsyncClient` along with `pytest-asyncio` to simulate requests to the FastAPI application. The tests are designed to run without needing the application to be deployed as a microservice.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
