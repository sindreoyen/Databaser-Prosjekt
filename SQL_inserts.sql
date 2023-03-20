
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
