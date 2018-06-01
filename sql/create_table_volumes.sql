-- Table: cryptos.volumes

-- DROP TABLE cryptos.volumes;

CREATE TABLE cryptos.volumes
(
    "timestamp" timestamp without time zone NOT NULL,
    exchange character varying COLLATE pg_catalog."default" NOT NULL,
    currency_pair character varying COLLATE pg_catalog."default" NOT NULL,
    currency_tag_1 character varying COLLATE pg_catalog."default" NOT NULL,
    volume_currency_1 double precision,
    currency_tag_2 character varying COLLATE pg_catalog."default" NOT NULL,
    volume_currency_2 double precision,
    CONSTRAINT volumes_pkey PRIMARY KEY ("timestamp", exchange, currency_pair)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE cryptos.volumes
    OWNER to postgres;

-- Index: volumes_idx

-- DROP INDEX cryptos.volumes_idx;

CREATE UNIQUE INDEX volumes_idx
    ON cryptos.volumes USING btree
    ("timestamp", currency_pair COLLATE pg_catalog."default")
    TABLESPACE pg_default;