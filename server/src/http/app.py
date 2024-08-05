from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.http.routes.auth.auth import router as auth_router
from src.http.routes.reports.reports import router as reports_router

app = FastAPI()

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


app.include_router(auth_router)
app.include_router(reports_router)
