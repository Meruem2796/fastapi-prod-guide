# API with FastAPI and MongoDB

A modern, production-ready API built to demonstrate the power of **FastAPI** and **MongoDB**.

## 🚀 About the Project

This application exposes a fully asynchronous REST API to manage personal Todo items. It ships with authenticated, multi-user support, automatic interactive documentation, structured logging, and a production-grade deployment setup (Gunicorn, Docker, Kubernetes).

### Key Features

*   **⚡ Fully Asynchronous**: Built with FastAPI and the async Motor driver for MongoDB.
*   **✅ Todo Management**: Full CRUD (Create, Read, Update, Delete) endpoints for Todo items.
*   **🔐 GitHub OAuth Authentication**: Secure Bearer token authentication using GitHub's OAuth2 flow.
*   **🔒 Per-User Data Isolation**: Users only see and manage their own Todos.
*   **📖 Auto-Generated Docs**: Interactive Swagger UI generated automatically from Pydantic models.
*   **📊 Request Logging & Metrics**: Middleware for structured logging and response-time tracking.
*   **🧪 Fully Tested**: Unit and integration tests with Pytest, coverage reports, and a mocked MongoDB for CI.
*   **🐳 Production Ready**: Dockerized, load-balanced with Gunicorn/Uvicorn workers, deployable to Kubernetes.

## 🛠️ Technology Stack

*   **Framework**: [FastAPI](https://fastapi.tiangolo.com)
*   **Database**: [MongoDB](https://www.mongodb.com) via [Motor](https://motor.readthedocs.io) (async driver)
*   **Package Manager**: [Poetry](https://python-poetry.org)
*   **Authentication**: GitHub OAuth2 (Bearer tokens)
*   **Testing**: [Pytest](https://pytest.org) + [Coverage.py](https://coverage.readthedocs.io) + [mongomock-motor](https://pypi.org/project/mongomock-motor/)
*   **Server**: [Uvicorn](https://www.uvicorn.org) / [Gunicorn](https://gunicorn.org)
*   **Containerization**: Docker, Docker Compose, Kubernetes

## 🏁 Getting Started

### Prerequisites

*   Python 3.11+
*   [Poetry](https://python-poetry.org/docs/#installation)
*   [Docker](https://www.docker.com) (for running MongoDB locally)

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Meruem2796/fastapi-prod-guide.git
    cd fastapi-prod-guide
    ```

2.  **Install dependencies**
    ```bash
    poetry install
    ```

3.  **Setup environment**

    Create a `.env` file at the project root:
    ```env
    MONGO_INITDB_ROOT_USERNAME=USER
    MONGO_INITDB_ROOT_PASSWORD=PASSWORD
    MONGO_URI=mongodb://USERt:PASSWORD@localhost:27017/
    GITHUB_OAUTH_CLIENT_ID=XXX
    GITHUB_OAUTH_CLIENT_SECRET=XXX
    ```

4.  **Start MongoDB**
    ```bash
    docker-compose up -d db
    ```

5.  **Run the API**
    ```bash
    poetry run python -m app.main
    ```

Visit `http://localhost:8000/` to view the interactive Swagger documentation, or `http://localhost:8000/v1/todos` to hit the API directly (Bearer token required).

## 🔑 Authentication

This API uses GitHub OAuth2 to authenticate users:

1.  Open the authorization link shown in the API description at `http://localhost:8000/`.
2.  Authorize the app on GitHub.
3.  GitHub redirects to `/v1/auth/callback`, which returns an access token.
4.  Use that token as a Bearer token on subsequent requests:
    ```bash
    curl http://localhost:8000/v1/todos \
      -H "Authorization: Bearer <your_access_token>"
    ```

## 📚 API Endpoints

| Method | Endpoint          | Description             |
|--------|-------------------|--------------------------|
| GET    | `/v1/auth/callback` | GitHub OAuth callback |
| POST   | `/v1/todos`        | Create a new Todo       |
| GET    | `/v1/todos`        | List all Todos (current user) |
| GET    | `/v1/todos/{id}`   | Get a single Todo       |
| PUT    | `/v1/todos/{id}`   | Update a Todo           |
| DELETE | `/v1/todos/{id}`   | Delete a Todo           |

## 🧪 Running Tests

```bash
export TESTING=true
poetry run coverage run --source ./app -m pytest --disable-warnings
poetry run coverage html
```

Open `htmlcov/index.html` in your browser to view the coverage report.

## 🐳 Running with Docker Compose

```bash
docker-compose up
```

This starts both the MongoDB instance and the API, available at `http://localhost:8000`.

## ☁️ Production Deployment

*   **Docker**: A multi-stage `Dockerfile` builds a lean production image served by Gunicorn with Uvicorn workers.
*   **Kubernetes**: `deployment.yaml`, `mongo.yaml` and `service.yaml` manifests are provided for scaling across multiple pods, with secrets managed via `kubectl create secret`.
*   **NGINX**: An `nginx.conf` example is included for single-node HTTPS termination and reverse proxying.

## 📝 License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).