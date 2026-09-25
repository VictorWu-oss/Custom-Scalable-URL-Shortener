from collections.abc import Iterator
from contextlib import contextmanager

import psycopg

from .domain import Link


class PostgresLinkRepository:
    def __init__(self, database_url: str) -> None:
        self.database_url = database_url

    @contextmanager
    def _connection(self) -> Iterator[psycopg.Connection]:
        with psycopg.connect(self.database_url) as connection:
            yield connection

    def find_by_hash(self, url_hash: str) -> Link | None:
        with self._connection() as connection:
            row = connection.execute(
                """
                SELECT short_code, destination_url, url_hash, created_at
                FROM links
                WHERE url_hash = %s
                """,
                (url_hash,),
            ).fetchone()
        return self._to_link(row) if row else None

    def find_by_code(self, code: str) -> Link | None:
        with self._connection() as connection:
            row = connection.execute(
                """
                SELECT short_code, destination_url, url_hash, created_at
                FROM links
                WHERE short_code = %s
                """,
                (code,),
            ).fetchone()
        return self._to_link(row) if row else None

    def save(self, link: Link) -> Link:
        with self._connection() as connection:
            row = connection.execute(
                """
                INSERT INTO links (short_code, destination_url, url_hash)
                VALUES (%s, %s, %s)
                ON CONFLICT (url_hash) DO UPDATE
                    SET url_hash = EXCLUDED.url_hash
                RETURNING short_code, destination_url, url_hash, created_at
                """,
                (link.code, link.destination, link.url_hash),
            ).fetchone()
        assert row is not None
        return self._to_link(row)

    @staticmethod
    def _to_link(row: tuple[object, ...]) -> Link:
        code, destination, url_hash, created_at = row
        return Link(
            code=str(code),
            destination=str(destination),
            url_hash=str(url_hash),
            created_at=created_at,  # type: ignore[arg-type]
        )

