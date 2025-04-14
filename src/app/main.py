from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import login_check_router
# Создаем приложение
app = FastAPI(
    title="FastAPI Application",
    description="API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login_check_router, prefix="/api/v1")
