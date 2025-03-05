# Folder Structure explanation

---
A good folder structure helps keep your Python web server organized, scalable, and maintainable. Here’s a recommended structure, similar to how an Express.js project is organized.

## 📂 Recommended Folder Structure

```
my_project/
│── app/
│   ├── routers/
│   │   ├── users.py
│   │   ├── products.py
│   │   ├── __init__.py
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── __init__.py
│   ├── services/
│   │   ├── auth.py
│   │   ├── database.py
│   │   ├── __init__.py
│   ├── __init__.py
│── config/
│   ├── settings.py
│── tests/
│   ├── test_users.py
│   ├── test_products.py
│── main.py
│── requirements.txt
│── .env
│── README.md
```

## 📌 Explanation of Each Folder

### 1️⃣ `app/` (Main Application Folder)
Holds all core application logic.

### 📂 `routers/` (Handles Routes & Endpoints)
Like `routes` in Express.js from a project in Node.js (Javascript), it contains API route definitions.

```
# app/routers/users.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"id": 1, "name": "John Doe"}]
```

### 📂 `models/` (Database Models & Schemas)
Like `models` in Express.js from a project in Node.js (Javascript), it defines database structure.

```
# app/models/user.py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
```

### 📂 `services/` (Business Logic & Database Layer)
Handles database queries, authentication, and reusable functions.

```
# app/services/database.py
import oracledb

def get_db_connection():
    return oracledb.connect(user="user", password="pass", dsn="localhost/XE")
```

### 2️⃣ `config/` (Configuration Files)
Handles environment variables and app settings.

```
# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
```

### 3️⃣ `tests/` (Unit Tests)
Contains test cases for API routes.

```
# tests/test_users.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
```

### 4️⃣ `main.py` (Entry Point)
Starts the FastAPI/Flask server.

```
# main.py
from fastapi import FastAPI
from app.routers import users

app = FastAPI()
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

### 5️⃣ `.env` (Environment Variables)
Keeps sensitive data secret (e.g., database credentials).

```
DATABASE_URL=oracle+oracledb://user:password@localhost:1521/XE
SECRET_KEY=mysecret
```

## 🔥 Why Use This Structure?
- ✅ **Separation of Concerns (Routers, Models, Services)**
- ✅ **Scalable & Maintainable (Easier to add features)**
- ✅ **Best Practices (Inspired by Express.js & Django)**