## BlogPost App using FastAPI

**Introduction**

This is a simple blog post application built with FastAPI, a modern Python web framework. The app allows users to create, read, update, and delete blog posts.

**Features**

* User authentication: Users can create accounts and log in.
* CRUD operations: Users can create, read, update, and delete blog posts.
* User-friendly API documentation: The app comes with built-in Swagger UI for easy API exploration.

**Prerequisites**

Before you begin, ensure you have met the following requirements:

* Python 3.6 or higher installed.
* `pip` package manager installed.
* [Poetry](https://python-poetry.org/) for dependency management (optional but recommended).

**Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/blogpost-app.git
cd blogpost-app
```

2. Set up a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the project dependencies:

Using Poetry (recommended):
```bash
poetry install
```

Using pip:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root and configure the following environment variables:
```
# Database configuration
SQLALCHEMY_DATABASE_URL=postgresql://user:password@localhost/dbname

# JWT secret key (generate a secure random key)
SECRET_KEY=your_secret_key

# JWT Algorithm 
ALGORITHM=your_algorithm

#JWT token expiration time
ACCESS_TOKEN_EXPIRE_MINUTES=your_preferred_time_limit

```

**Usage**
1. Start the FastAPI server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
2. Access the Swagger API documentation at http://localhost:8000/docs in your web browser.

**Contributing**

Contributions are welcome! Please follow our contribution guidelines.

**License**

This project is licensed under the Apache-2.0 license. See the LICENSE file for details.
