CREATE TABLE links (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    short_code VARCHAR(16) NOT NULL,
    destination_url TEXT NOT NULL,
    url_hash CHAR(64) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    redirect_count BIGINT NOT NULL DEFAULT 0,

    CONSTRAINT links_short_code_unique UNIQUE (short_code),
    CONSTRAINT links_url_hash_unique UNIQUE (url_hash),
    CONSTRAINT links_redirect_count_non_negative CHECK (redirect_count >= 0)
);

CREATE INDEX links_created_at_idx ON links (created_at);

