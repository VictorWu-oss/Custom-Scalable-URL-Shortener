from fastapi import FastAPI, Request

from .api import CreateLinkRequest, CreateLinkResponse, create_link
from .repository import InMemoryLinkRepository
from .service import LinkService

app = FastAPI(title="URL Shortener", version="0.1.0")
service = LinkService(InMemoryLinkRepository())


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/links", response_model=CreateLinkResponse, status_code=201)
def create(request: CreateLinkRequest, http_request: Request) -> CreateLinkResponse:
    return create_link(service, request, str(http_request.base_url))
