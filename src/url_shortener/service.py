import hashlib

from .base62 import encode
from .domain import Link, utc_now
from .repository import InMemoryLinkRepository


class LinkService:
    def __init__(self, repository: InMemoryLinkRepository) -> None:
        self.repository = repository

    def create_link(self, destination: str) -> Link:
        url_hash = hashlib.sha256(destination.encode("utf-8")).hexdigest()
        existing = self.repository.find_by_hash(url_hash)
        if existing is not None:
            return existing

        # The hash-derived number makes this first implementation deterministic.
        code = encode(int(url_hash[:16], 16))
        link = Link(code=code, destination=destination, url_hash=url_hash, created_at=utc_now())
        return self.repository.save(link)
