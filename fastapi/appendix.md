# Appendices

[← Back to TOC](./TOC.md)

---

## Appendix A: FastAPI Quick Reference

### Minimal App

```python
from fastapi import FastAPI

app = FastAPI(title="My API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Run with: `uvicorn main:app --reload`

### Path and Query Parameters

```python
from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

# Path parameter — part of the URL
@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(description="The ID of the item", ge=1),
    q: Optional[str] = Query(default=None, max_length=50),
):
    return {"item_id": item_id, "q": q}
```

### Request Body with Pydantic

```python
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0, description="Must be positive")
    description: Optional[str] = None
    is_available: bool = True

@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    return item
```

### Dependency Injection

```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def require_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admins only")
    return current_user

@app.get("/admin/users")
async def list_users(
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
):
    return db.query(User).all()
```

### Error Handling

```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request

# Simple HTTP error
raise HTTPException(status_code=404, detail="Item not found")

# Custom exception handler
class AppException(Exception):
    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.code,
        content={"error": exc.message},
    )
```

### Authentication (JWT)

```python
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return get_user(username)
```

### Middleware

```python
from fastapi.middleware.cors import CORSMiddleware
import time

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start)
    return response
```

### Background Tasks

```python
from fastapi import BackgroundTasks

def send_email(address: str, message: str):
    # This runs after the response is sent
    email_client.send(address, message)

@app.post("/register")
async def register(user: UserCreate, tasks: BackgroundTasks):
    new_user = create_user(user)
    tasks.add_task(send_email, new_user.email, "Welcome!")
    return new_user
```

---

## Appendix B: Python Type Hints Reference

```python
from typing import Optional, Union, List, Dict, Tuple, Any, Callable
from typing import TypeVar, Generic, Annotated, Literal
from collections.abc import Sequence, Mapping

# Basic
x: int = 5
name: str = "Alice"
pi: float = 3.14
flag: bool = True

# Optional (can be None)
email: Optional[str] = None   # same as: str | None  (Python 3.10+)

# Collections
items: list[int] = [1, 2, 3]
mapping: dict[str, int] = {"a": 1}
pair: tuple[int, str] = (1, "one")

# Union (one of several types)
id: int | str = "abc-123"      # Python 3.10+
id: Union[int, str] = "abc-123"  # older syntax

# Callable
handler: Callable[[int, str], bool]

# TypeVar (for generics)
T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

# Annotated (add metadata for validation)
from pydantic import Field
Price = Annotated[float, Field(gt=0, description="Must be positive")]

# Literal (only specific values)
Direction = Literal["north", "south", "east", "west"]

# TypedDict
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: float
```

---

## Appendix C: CLI and Tooling Reference

```bash
# Start development server with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Start with multiple workers (production)
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000

# Or with gunicorn + uvicorn workers
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker

# Run tests
pytest tests/ -v
pytest tests/ --cov=app --cov-report=html

# Type checking
mypy app/

# Linting and formatting
ruff check app/
ruff format app/

# Generate OpenAPI JSON
python -c "from main import app; import json; print(json.dumps(app.openapi(), indent=2))" > openapi.json
```

---

## Appendix D: Common Pitfalls and FAQ

### 1. Mixing async and sync code

```python
# WRONG — blocks the event loop
@app.get("/items")
async def get_items():
    time.sleep(2)           # blocking! freezes all other requests
    return items

# CORRECT — use async sleep, or move blocking code to a thread pool
import asyncio
@app.get("/items")
async def get_items():
    await asyncio.sleep(2)  # non-blocking
    return items

# For CPU-bound or legacy sync code, use run_in_executor
import asyncio
from concurrent.futures import ThreadPoolExecutor

@app.get("/heavy")
async def heavy():
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, heavy_sync_function)
    return result
```

### 2. Dependency scope confusion

FastAPI dependencies run on every request by default. To share expensive resources (like DB connections), use `yield` with proper cleanup — the code after `yield` runs after the response is sent.

### 3. Response model validation

When you set `response_model=UserOut`, FastAPI will serialize and validate the response against that model, automatically excluding fields not in `UserOut` (like passwords). This is a security feature — use it.

---

## Glossary

**ASGI (Asynchronous Server Gateway Interface)**
The Python standard for async web servers and apps. FastAPI is an ASGI application. Uvicorn is an ASGI server. ASGI allows handling many simultaneous requests without blocking.

**Coroutine**
An async function defined with `async def`. Calling it returns a coroutine object — it doesn't run until you `await` it. Coroutines allow pausing execution while waiting for I/O without blocking the thread.

**Path Operation**
FastAPI's term for a route handler — a function decorated with `@app.get()`, `@app.post()`, etc. The "path" is the URL pattern; the "operation" is the HTTP method.

**Dependency Injection**
A pattern where a function declares what it needs (its dependencies), and the framework creates and provides them. In FastAPI, `Depends(get_db)` tells FastAPI to call `get_db()` and pass the result to your function.

**OpenAPI**
A standard specification format for describing REST APIs. FastAPI automatically generates an OpenAPI document from your code, which it uses to serve interactive docs at `/docs` (Swagger UI) and `/redoc`.

**Pydantic**
A Python library for data validation using type annotations. When you define a `BaseModel`, Pydantic automatically validates, coerces, and serializes data. FastAPI uses Pydantic for all request and response models.
