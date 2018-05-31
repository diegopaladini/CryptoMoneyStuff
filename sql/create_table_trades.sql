-- Table: cryptos.trades

-- DROP TABLE cryptos.trades;

CREATE TABLE cryptos.trades
(
    exchange character varying(128) COLLATE pg_catalog."default" NOT NULL,
    currency character varying(3) COLLATE pg_catalog."default" NOT NULL,
    open_date timestamp without time zone NOT NULL,
    close_date timestamp without time zone,
    volume double precision NOT NULL,
    price_buy double precision NOT NULL,
    price_sell double precision,
    isopen integer NOT NULL,
    fee double precision NOT NULL,
    pos_id bigint NOT NULL,
    currency_buy character varying(3) COLLATE pg_catalog."default",
    currency_sell character varying(3) COLLATE pg_catalog."default",
    currency_buy_euro_value double precision,
    currency_buy_euro_sell double precision,
    CONSTRAINT trades_pkey PRIMARY KEY (pos_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE cryptos.trades
    OWNER to postgres;

-- Index: trades_idx

-- DROP INDEX cryptos.trades_idx;

CREATE UNIQUE INDEX trades_idx
    ON cryptos.trades USING btree
    (exchange COLLATE pg_catalog."default", currency COLLATE pg_catalog."default")
    TABLESPACE pg_default;

ALTER TABLE cryptos.trades
    CLUSTER ON trades_idx;