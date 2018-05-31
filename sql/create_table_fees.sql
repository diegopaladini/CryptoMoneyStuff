-- Table: cryptos.fees

-- DROP TABLE cryptos.fees;

CREATE TABLE cryptos.fees
(
    exchange character varying(128) COLLATE pg_catalog."default" NOT NULL,
    fee double precision,
    currency character varying(3) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT fees_pkey PRIMARY KEY (exchange, currency)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE cryptos.fees
    OWNER to postgres;