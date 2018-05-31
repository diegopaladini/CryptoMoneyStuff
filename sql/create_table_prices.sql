-- Table: cryptos.prices

-- DROP TABLE cryptos.prices;

CREATE TABLE cryptos.prices
(
    "timestamp" timestamp without time zone NOT NULL,
    exchange character varying COLLATE pg_catalog."default" NOT NULL,
    currency_pair character varying COLLATE pg_catalog."default" NOT NULL,
    open double precision,
    close double precision,
    high double precision,
    low double precision,
    weighted_average double precision,
    base_volume double precision,
    quote_volume double precision,
    currency_tag character varying(16) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE cryptos.prices
    OWNER to postgres;

-- Index: prices_idx

-- DROP INDEX cryptos.prices_idx;

CREATE UNIQUE INDEX prices_idx
    ON cryptos.prices USING btree
    ("timestamp", currency_pair COLLATE pg_catalog."default")
    TABLESPACE pg_default;