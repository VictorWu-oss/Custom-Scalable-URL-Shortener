from urllib.parse import urlparse

from pydantic import BaseModel, field_validator

from .service import LinkService


class CreateLinkRequest(BaseModel):
    url: str

    @field_validator("url")
    @classmethod
    def validate_url(cls, value: str) -> str:
        parsed = urlparse(value)
        if (
            parsed.scheme not in {"http", "https"}
            or not parsed.netloc
            or any(character.isspace() for character in value)
        ):
            raise ValueError("url must be an HTTP or HTTPS URL")
        return value


class CreateLinkResponse(BaseModel):
    code: str
    short_url: str
    destination: str


def create_link(service: LinkService, request: CreateLinkRequest, base_url: str) -> CreateLinkResponse:
    link = service.create_link(str(request.url))
    return CreateLinkResponse(
        code=link.code,
        short_url=f"{base_url.rstrip('/')}/{link.code}",
        destination=link.destination,
    )
