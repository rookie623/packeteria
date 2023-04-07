-- Table: public.packetes

-- DROP TABLE IF EXISTS public.packetes;

CREATE SEQUENCE packetes_id_seq;

CREATE TABLE IF NOT EXISTS public.packetes
(
    id bigint NOT NULL DEFAULT nextval('packetes_id_seq'),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    lastname character varying COLLATE pg_catalog."default" NOT NULL,
    lote character varying COLLATE pg_catalog."default" NOT NULL,
    turno character varying COLLATE pg_catalog."default" NOT NULL,
    es_retirado boolean NOT NULL DEFAULT false,
    created_at time with time zone NOT NULL DEFAULT now(),
    CONSTRAINT packetes_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.packetes
    OWNER to postgres;