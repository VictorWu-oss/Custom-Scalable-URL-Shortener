from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Link:
    code: str
    destination: str
    url_hash: str
    created_at: datetime


def utc_now() -> datetime:
    return datetime.now(timezone.utc)

