-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2025-02-14 16:41:55 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE cargo CASCADE CONSTRAINTS;

DROP TABLE categoria_prod CASCADE CONSTRAINTS;

DROP TABLE depto CASCADE CONSTRAINTS;

DROP TABLE funcionario CASCADE CONSTRAINTS;

DROP TABLE tarefas CASCADE CONSTRAINTS;

DROP TABLE tarefas_func CASCADE CONSTRAINTS;

DROP TABLE tipo_tarefa CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE cargo (
    cd_cargo NUMBER(3) NOT NULL,
    ds_cargo VARCHAR2(50) UNIQUE NOT NULL
)
LOGGING;

ALTER TABLE cargo ADD CONSTRAINT cargo_pk PRIMARY KEY ( cd_cargo );

CREATE TABLE categoria_prod (
    cd_categoria   NUMBER(5) NOT NULL,
    cd_tipo_tarefa NUMBER(2) NOT NULL,
    ds_categoria   VARCHAR2(500) UNIQUE NOT NULL
)
LOGGING;

COMMENT ON COLUMN categoria_prod.cd_categoria IS
    'Essa coluna ira armazenar a chave primaria da tabela de categoria de produtos da Melhorees Compras. Cada categoria nova cadastrada  ser� acionada a Sequence  SQ_CATEGORIA que se encarregar� de gerar o pr�ximo n�mero �nico da categoria..'
    ;

COMMENT ON COLUMN categoria_prod.ds_categoria IS
    'Essa coluna ira armazenar descricao da categoria de produtos da Melhorees Compras. Cada categoria tem uma  descri��o �nica e serve para organizar os produtos em categorias simliares, melhorando a tomada de decis�o.'
    ;

ALTER TABLE categoria_prod ADD CONSTRAINT categoria_prod_pk PRIMARY KEY ( cd_categoria );

CREATE TABLE depto (
    cd_depto NUMBER(3) NOT NULL,
    nm_depto VARCHAR2(100) UNIQUE NOT NULL
)
LOGGING;

COMMENT ON COLUMN depto.cd_depto IS
    'Esta coluna ir� receber o codigo do departamento  e seu conte�do � obrigat�rio.';

COMMENT ON COLUMN depto.nm_depto IS
    'Esta coluna ir� receber o nome do  departamento  e seu conte�do � obrigat�rio.';


ALTER TABLE depto ADD CONSTRAINT depto_pk PRIMARY KEY ( cd_depto );

CREATE TABLE funcionario (
    cd_funcionario     VARCHAR(10) UNIQUE NOT NULL,
    cd_depto           NUMBER(3) NOT NULL,
    cd_cargo           NUMBER(3) NOT NULL,
    ds_email           VARCHAR2(80) NOT NULL,
    ps_password        VARCHAR2(20) NOT NULL,
    cd_gerente         NUMBER,
    nm_funcionario     VARCHAR2(160) NOT NULL,
    dt_cadastramento   DATE NOT NULL
)
LOGGING;

COMMENT ON COLUMN funcionario.cd_funcionario IS
    'Esta coluna ir� receber o codigo do funcion�rio e seu conte�do � obrigat�rio.';

COMMENT ON COLUMN funcionario.ds_email IS
    'Esta coluna ir� receber o email do funcion�rio.';

COMMENT ON COLUMN funcionario.cd_gerente IS
    'Esta coluna ir� receber o codigo do gestor do funcionario trabalha  e seu conte�do � opcional.';

COMMENT ON COLUMN funcionario.nm_funcionario IS
    'Esta coluna ir� receber o nome do funcion�rio e seu conte�do � obrigat�rio.';

COMMENT ON COLUMN funcionario.dt_cadastramento IS
    'Data de cadastramento do Funcionario';

CREATE TABLE tarefas (
    cd_tarefas     NUMBER(5) NOT NULL,
    cd_tipo_tarefa NUMBER(2) NOT NULL,
    ds_tarefas     VARCHAR2(50) NOT NULL
)
LOGGING;

ALTER TABLE tarefas ADD CONSTRAINT tarefas_pk PRIMARY KEY ( cd_tarefas );

CREATE TABLE tarefas_func (
    cd_tarefa_func NUMBER(5) NOT NULL,
    cd_tarefas     NUMBER(5) NOT NULL,
    cd_funcionario VARCHAR(10) NOT NULL
)
LOGGING;

ALTER TABLE tarefas_func ADD CONSTRAINT tarefas_func_pk PRIMARY KEY ( cd_tarefa_func );

CREATE TABLE tipo_tarefa (
    cd_tipo_tarefa NUMBER(2) NOT NULL,
    ds_tipo_tarefa VARCHAR (50) NOT NULL
)
LOGGING;

ALTER TABLE tipo_tarefa ADD CONSTRAINT tipo_tarefa_pk PRIMARY KEY ( cd_tipo_tarefa );

ALTER TABLE categoria_prod
    ADD CONSTRAINT cat_prod FOREIGN KEY ( cd_tipo_tarefa )
        REFERENCES tipo_tarefa ( cd_tipo_tarefa )
    NOT DEFERRABLE;

ALTER TABLE funcionario
    ADD CONSTRAINT func_cargo FOREIGN KEY ( cd_cargo )
        REFERENCES cargo ( cd_cargo )
    NOT DEFERRABLE;

ALTER TABLE funcionario
    ADD CONSTRAINT pk_dpto FOREIGN KEY ( cd_depto )
        REFERENCES depto ( cd_depto )
    NOT DEFERRABLE;

ALTER TABLE tarefas_func
    ADD CONSTRAINT tarefas FOREIGN KEY ( cd_tarefas )
        REFERENCES tarefas ( cd_tarefas )
    NOT DEFERRABLE;

ALTER TABLE tarefas_func
    ADD CONSTRAINT tarefas_func FOREIGN KEY ( cd_funcionario )
        REFERENCES funcionario ( cd_funcionario )
    NOT DEFERRABLE;

ALTER TABLE tarefas
    ADD CONSTRAINT tipo_tarefa FOREIGN KEY ( cd_tipo_tarefa )
        REFERENCES tipo_tarefa ( cd_tipo_tarefa )
    NOT DEFERRABLE;


DROP SEQUENCE SEQ_CARGO;
DROP SEQUENCE SEQ_CD_CAT_PROD;
DROP SEQUENCE SEQ_DEPTO;
DROP SEQUENCE SEQ_TAREFAS;
DROP SEQUENCE SEQ_TIPO_TAREFA;

DROP TRIGGER TRIG_SEQ_CARGO;
DROP TRIGGER TRIG_SEQ_CD_CAT_PROD;
DROP TRIGGER TRIG_SEQ_DEPTO;
DROP TRIGGER TRIG_SEQ_TAREFAS;
DROP TRIGGER TRIG_SEQ_TIPO_TAREFA;



CREATE SEQUENCE SEQ_CARGO
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE TRIGGER TRIG_SEQ_CARGO
BEFORE INSERT ON CARGO
FOR EACH ROW 
BEGIN IF :NEW.CD_CARGO IS NULL THEN
SELECT SEQ_CARGO.NEXTVAL INTO :NEW.CD_CARGO FROM DUAL;
END IF;
END;


CREATE SEQUENCE SEQ_CD_CAT_PROD
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE TRIGGER TRIG_SEQ_CD_CAT_PROD
BEFORE INSERT ON CATEGORIA_PROD
FOR EACH ROW 
BEGIN IF :NEW.CD_CATEGORIA IS NULL THEN
SELECT SEQ_CD_CAT_PROD.NEXTVAL INTO :NEW.CD_CATEGORIA FROM DUAL;
END IF;
END;

CREATE SEQUENCE SEQ_DEPTO
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE TRIGGER TRIG_SEQ_DEPTO
BEFORE INSERT ON DEPTO
FOR EACH ROW 
BEGIN IF :NEW.CD_DEPTO IS NULL THEN
SELECT SEQ_DEPTO.NEXTVAL INTO :NEW.CD_DEPTO FROM DUAL;
END IF;
END;

CREATE SEQUENCE SEQ_TAREFAS
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE TRIGGER TRIG_SEQ_TAREFAS
BEFORE INSERT ON TAREFAS
FOR EACH ROW 
BEGIN IF :NEW.CD_TAREFAS IS NULL THEN
SELECT SEQ_TAREFAS.NEXTVAL INTO :NEW.CD_TAREFAS FROM DUAL;
END IF;
END;


CREATE SEQUENCE SEQ_TIPO_TAREFA
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

CREATE OR REPLACE TRIGGER TRIG_SEQ_TIPO_TAREFA
BEFORE INSERT ON TIPO_TAREFA
FOR EACH ROW 
BEGIN IF :NEW.CD_TIPO_TAREFA IS NULL THEN
SELECT SEQ_TIPO_TAREFA.NEXTVAL INTO :NEW.CD_TIPO_TAREFA FROM DUAL;
END IF;
END;



DELETE FROM cargo;
DELETE FROM categoria_prod;
DELETE FROM depto;
DELETE FROM tipo_tarefa;


INSERT INTO cargo (ds_cargo) VALUES ('gerente');
INSERT INTO cargo (ds_cargo) VALUES ('repositor');
INSERT INTO cargo (ds_cargo) VALUES ('caixa');

INSERT INTO tipo_tarefa (ds_tipo_tarefa) VALUES ('organizacao');
INSERT INTO tipo_tarefa (ds_tipo_tarefa) VALUES ('contabilidade');
INSERT INTO tipo_tarefa (ds_tipo_tarefa) VALUES ('venda');


INSERT INTO CATEGORIA_PROD (ds_categoria, cd_tipo_tarefa) VALUES ('limpeza', 1);
INSERT INTO CATEGORIA_PROD (ds_categoria, cd_tipo_tarefa) VALUES ('alimento', 1);
INSERT INTO CATEGORIA_PROD (ds_categoria, cd_tipo_tarefa) VALUES ('bebida', 1);
INSERT INTO CATEGORIA_PROD (ds_categoria, cd_tipo_tarefa) VALUES ('feira', 1);

INSERT INTO depto (nm_depto) VALUES ('operacoes');

COMMIT;



/

-- Relat�rio do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             0
-- ALTER TABLE                             14
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           1
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          1
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
