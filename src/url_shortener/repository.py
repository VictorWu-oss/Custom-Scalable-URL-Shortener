from collections.abc import Mapping

from .domain import Link


class InMemoryLinkRepository:
    def __init__(self) -> None:
        self._by_code: dict[str, Link] = {}
        self._by_hash: dict[str, Link] = {}

    def find_by_hash(self, url_hash: str) -> Link | None:
        return self._by_hash.get(url_hash)

    def find_by_code(self, code: str) -> Link | None:
        return self._by_code.get(code)

    def save(self, link: Link) -> Link:
        self._by_code[link.code] = link
        self._by_hash[link.url_hash] = link
        return link

    @property
    def links(self) -> Mapping[str, Link]:
        return self._by_code
