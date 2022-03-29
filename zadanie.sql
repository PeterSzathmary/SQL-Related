-- Vytvorte pouzivatela AKCIE, nastavte mu default tablespace DATA (alebo ekvivalent u vas), dajte mu neobmedzenu kvotu na DATA (alebo ekvivalent), grantnite mu moznost prihlasenia a vytvorenia tabulky.
CREATE USER akcie IDENTIFIED BY Start123;

-- prihlasenie:
-- sqlplus akcie/Start123
-- connect akcie/Start123

ALTER USER akcie DEFAULT TABLESPACE DATA;
ALTER USER akcie QUOTA UNLIMITED ON DATA;

GRANT CREATE SESSION, CREATE TABLE TO akcie;

CONNECT akcie/Start123;

-- Vytvorte nasledujuce 3 tabulky LIDL, KAUFLAND a ZLAVY

-- Meno varchar2(30) | Typ varchar2(20) | Cena NUMBER |	Balenie CHAR(2)
CREATE TABLE LIDL
(
    Meno VARCHAR2(30) NOT NULL,
    Typ VARCHAR2(20) NOT NULL,
    Cena NUMBER NOT NULL,
    Balenie CHAR(2) NOT NULL
);

-- Meno varchar2(30) | Typ CHAR(3) | Cena NUMBER | Balenie CHAR(2)
CREATE TABLE KAUFLAND
(
    Meno VARCHAR2(30) NOT NULL,
    Typ CHAR(3) NOT NULL,
    Cena NUMBER NOT NULL,
    Balenie CHAR(2) NOT NULL
);

-- id NUMBER | Percento NUMBER | Datum DATE
CREATE TABLE ZLAVY
(
    ID NUMBER PRIMARY KEY NOT NULL,
    Percento NUMBER NOT NULL,
    Datum DATE NOT NULL
);

@inserts_lidl.sql
@inserts_kaufland.sql
@inserts_zlavy.sql