from url_shortener.repository import InMemoryLinkRepository
from url_shortener.service import LinkService
from url_shortener.api import CreateLinkRequest
from pydantic import ValidationError


def test_creating_same_url_is_idempotent() -> None:
    service = LinkService(InMemoryLinkRepository())

    first = service.create_link("https://example.com")
    second = service.create_link("https://example.com")

    assert first == second
    assert first.code


def test_urls_that_differ_by_one_character_are_distinct() -> None:
    service = LinkService(InMemoryLinkRepository())

    first = service.create_link("https://example.com")
    second = service.create_link("https://example.com/")

    assert first.code != second.code
    assert first.destination != second.destination


def test_only_http_and_https_urls_are_valid() -> None:
    assert CreateLinkRequest(url="http://example.com").url == "http://example.com"
    assert CreateLinkRequest(url="https://example.com").url == "https://example.com"

    for value in ["ftp://example.com", "example.com", "https://"]:
        try:
            CreateLinkRequest(url=value)
        except ValidationError:
            continue
        raise AssertionError(f"expected validation failure for {value}")
