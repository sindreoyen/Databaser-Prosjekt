INSERT INTO "main"."Jernbanestasjon" ("navn", "moh") VALUES ('Bodø', '4.1');
INSERT INTO "main"."Jernbanestasjon" ("navn", "moh") VALUES ('Fauske', '34');
INSERT INTO "main"."Jernbanestasjon" ("navn", "moh") VALUES ('Mo i Rana', '3.5');
INSERT INTO "main"."Jernbanestasjon" ("navn", "moh") VALUES ('Mosjøen', '6.8');
INSERT INTO "main"."Jernbanestasjon" ("navn", "moh") VALUES ('Steinkjer', '3.6');
INSERT INTO "main"."Jernbanestasjon" ("navn", "moh") VALUES ('Trondheim S', '5.1');


INSERT INTO "main"."Operatør" ("operatørNavn") VALUES ('SJ');

INSERT INTO "main"."Banestrekning" ("strekningID", "navn", "fremdriftsenergi", "startstasjonNavn", "sluttstasjonNavn") VALUES ('1', 'Nordlandsbanen', 'diesel', 'Trondheim S', 'Bodø');

INSERT INTO "main"."Delstrekning"
("sportype", "lengde", "stasjon1", "stasjon2")
VALUES ("dobbelt", 120, "Trondheim S", "Steinkjer");

INSERT INTO "main"."Delstrekning"
("sportype", "lengde", "stasjon1", "stasjon2")
VALUES ("enkelt", 280, "Steinkjer", "Mosjøen");

INSERT INTO "main"."Delstrekning"
("sportype", "lengde", "stasjon1", "stasjon2")
VALUES ("enkelt", 90, "Mosjøen", "Mo i Rana");

INSERT INTO "main"."Delstrekning"
("sportype", "lengde", "stasjon1", "stasjon2")
VALUES ("enkelt", 170, "Mo i Rana", "Fauske");

INSERT INTO "main"."Delstrekning"
("sportype", "lengde", "stasjon1", "stasjon2")
VALUES ("enkelt", 60, "Fauske", "Bodø");

INSERT INTO "main"."HarDelstrekning"
("strekningID", "delstrekningID")
VALUES (1, 1);

INSERT INTO "main"."HarDelstrekning"
("strekningID", "delstrekningID")
VALUES (1, 2);

INSERT INTO "main"."HarDelstrekning"
("strekningID", "delstrekningID")
VALUES (1, 3);

INSERT INTO "main"."HarDelstrekning"
("strekningID", "delstrekningID")
VALUES (1, 4);

INSERT INTO "main"."HarDelstrekning"
("strekningID", "delstrekningID")
VALUES (1, 5);

INSERT INTO "main"."SovevognType" ("type", "antallKupeer") VALUES ('SJ-sovevogn-1', '4');

INSERT INTO "main"."SittevognType" ("type", "seterPrRad", "antallRader") VALUES ('SJ-sittevogn-1', '4', '3');


INSERT INTO "main"."Ukedag"
("navn")
VALUES ('man');

INSERT INTO "main"."Ukedag"
("navn")
VALUES ('tir');

INSERT INTO "main"."Ukedag"
("navn")
VALUES ('ons');

INSERT INTO "main"."Ukedag"
("navn")
VALUES ('tor');

INSERT INTO "main"."Ukedag"
("navn")
VALUES ('fre');

INSERT INTO "main"."Ukedag"
("navn")
VALUES ('lør');

INSERT INTO "main"."Ukedag"
("navn")
VALUES ('søn');

INSERT INTO "main"."Vogn" ("vognID") VALUES ('1');
INSERT INTO "main"."Vogn" ("vognID") VALUES ('2');
INSERT INTO "main"."Vogn" ("vognID") VALUES ('3');
INSERT INTO "main"."Vogn" ("vognID") VALUES ('4');
INSERT INTO "main"."Vogn" ("vognID") VALUES ('5');

INSERT INTO "main"."Sittevogn"
("vognID", "type")
VALUES (1, 'SJ-sittevogn-1');

INSERT INTO "main"."Sittevogn"
("vognID", "type")
VALUES (2, 'SJ-sittevogn-1');

INSERT INTO "main"."Sittevogn"
("vognID", "type")
VALUES (3, 'SJ-sittevogn-1');

INSERT INTO "main"."Sittevogn"
("vognID", "type")
VALUES (4, 'SJ-sittevogn-1');

INSERT INTO "main"."Sovevogn"
("vognID", "type")
VALUES (5, 'SJ-sovevogn-1');

INSERT INTO "main"."Vognoppsett" ("oppsettID", "antallSovevogner", "antallSittevogner") VALUES ('1', '0', '2');
INSERT INTO "main"."Vognoppsett" ("oppsettID", "antallSovevogner", "antallSittevogner") VALUES ('2', '1', '1');
INSERT INTO "main"."Vognoppsett" ("oppsettID", "antallSovevogner", "antallSittevogner") VALUES ('3', '0', '1');

INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '1', '1');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '2', '2');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('2', '3', '1');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('2', '5', '2');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('3', '4', '1');

INSERT INTO "main"."Sovekupe"
("vognID", "kupeNR")
VALUES (5, 1);

INSERT INTO "main"."Sovekupe"
("vognID", "kupeNR")
VALUES (5, 2);

INSERT INTO "main"."Sovekupe"
("vognID", "kupeNR")
VALUES (5, 3);

INSERT INTO "main"."Sovekupe"
("vognID", "kupeNR")
VALUES (5, 4);

INSERT INTO "main"."Togrute" ("ruteID", "medHovedRetning", "operatørNavn", "oppsettID", "strekningID") VALUES ('1', '1', 'SJ', '1', '1');

INSERT INTO "main"."Togrute" ("ruteID", "medHovedRetning", "operatørNavn", "oppsettID", "strekningID") VALUES ('2', '1', 'SJ', '2', '1');

INSERT INTO "main"."Togrute" ("ruteID", "medHovedRetning", "operatørNavn", "oppsettID", "strekningID") VALUES ('3', '0', 'SJ', '3', '1');

INSERT INTO "main"."HarVogn"
("operatørNavn", "vognID")
VALUES ('SJ', 1);

INSERT INTO "main"."HarVogn"
("operatørNavn", "vognID")
VALUES ('SJ', 2);

INSERT INTO "main"."HarVogn"
("operatørNavn", "vognID")
VALUES ('SJ', 3);

INSERT INTO "main"."HarVogn"
("operatørNavn", "vognID")
VALUES ('SJ', 4);

INSERT INTO "main"."HarVogn"
("operatørNavn", "vognID")
VALUES ('SJ', 5);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('man', 1);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('tir', 1);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('ons', 1);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('tor', 1);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('fre', 1);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('man', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('tir', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('ons', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('tor', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('fre', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('lør', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('søn', 2);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('man', 3);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('tir', 3);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('ons', 3);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('tor', 3);

INSERT INTO "main"."GårPåUkedag"
("navn", "ruteID")
VALUES ('fre', 3);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 1, 28140, 35460);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 2, 35460, 44400);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 3, 44400, 52260);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 4, 52260, 60540);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 5, 60540, 63240);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 1, 83100, 3420);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 2, 3420, 16860);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 3, 16860, 21300);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 4, 21300, 29940);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 5, 29940, 32700);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (3, 1, 51180, 45060);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (3, 2, 45060, 33240);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (3, 3, 33240, 29460);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 1);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 2);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 3);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 4);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 5);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 6);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 7);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 8);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 9);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 10);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 11);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (1, 12);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 1);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 2);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 3);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 4);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 5);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 6);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 7);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 8);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 9);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 10);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 11);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (2, 12);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 1);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 2);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 3);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 4);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 5);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 6);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 7);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 8);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 9);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 10);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 11);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (3, 12);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 1);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 2);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 3);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 4);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 5);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 6);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 7);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 8);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 9);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 10);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 11);

INSERT INTO "main"."Sete"
("vognID", "seteNR")
VALUES (4, 12);

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato", "navn")
VALUES (1, 1680472800, "dagtog");

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato", "navn")
VALUES (1, 1680559200, "dagtog");

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato", "navn")
VALUES (2, 1680472800, "nattog");

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato", "navn")
VALUES (2, 1680559200, "nattog");

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato", "navn")
VALUES (3, 1680472800, "morgentog");

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato", "navn")
VALUES (3, 1680559200, "morgentog");

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 1, 1);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 2, 1);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 3, 2);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 4, 2);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 5, 3);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 6, 3);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 7, 4);

INSERT INTO "main"."Seng"
("vognID", "sengNR", "kupeNR")
VALUES (5, 8, 4);