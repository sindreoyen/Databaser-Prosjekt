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
INSERT INTO "main"."Vognoppsett" ("oppsettID", "antallSovevogner", "antallSittevogner") VALUES ('3', '1', '0');

INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '1', '1');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '2', '2');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '3', '1');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '5', '2');
INSERT INTO "main"."VognIOppsett" ("oppsettID", "vognID", "vognNR") VALUES ('1', '4', '1');

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
VALUES (1, 1, 0749, 0951);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 2, 0951, 1320);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 3, 1320, 1431);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 4, 1431, 1649);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (1, 5, 1649, 1734);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 1, 2305, 0057);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 2, 0057, 0441);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 3, 0441, 0555);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 4, 0555, 0819);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (2, 5, 0819, 0905);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (3, 1, 1413, 1231);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (3, 2, 1231, 0914);

INSERT INTO "main"."KjørerStrekning"
("ruteID", "delstrekningID", "tidStasjon1", "tidStasjon2")
VALUES (3, 3, 0914, 0811);

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
("ruteID", "dato")
VALUES (1, 1680472800);

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato")
VALUES (1, 1680559200);

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato")
VALUES (2, 1680472800);

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato")
VALUES (2, 1680559200);

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato")
VALUES (3, 1680472800);

INSERT INTO "main"."TogruteForekomst"
("ruteID", "dato")
VALUES (3, 1680559200);
