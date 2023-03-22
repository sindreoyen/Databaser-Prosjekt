BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Vognoppsett" (
	"oppsettID"	INTEGER NOT NULL UNIQUE,
	"antallSovevogner"	INTEGER NOT NULL,
	"antallSittevogner"	INTEGER NOT NULL,
	PRIMARY KEY("oppsettID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Operatør" (
	"operatørNavn"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("operatørNavn")
);
CREATE TABLE IF NOT EXISTS "SittevognType" (
	"type"	TEXT NOT NULL UNIQUE,
	"seterPrRad"	INTEGER NOT NULL,
	"antallRader"	INTEGER NOT NULL,
	PRIMARY KEY("type")
);
CREATE TABLE IF NOT EXISTS "Sete" (
	"vognID"	INTEGER NOT NULL,
	"seteNR"	INTEGER NOT NULL,
	FOREIGN KEY("vognID") REFERENCES "Sittevogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("vognID","seteNR")
);
CREATE TABLE IF NOT EXISTS "Jernbanestasjon" (
	"navn"	TEXT NOT NULL UNIQUE,
	"moh"	INTEGER,
	PRIMARY KEY("navn")
);
CREATE TABLE IF NOT EXISTS "TogruteForekomst" (
	"ruteID"	INTEGER NOT NULL,
	"dato"	INTEGER NOT NULL CHECK("dato" > 0),
	"navn" TEXT NOT NULL,
	FOREIGN KEY("ruteID") REFERENCES "Togrute"("ruteID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("ruteID","dato")
);
CREATE TABLE IF NOT EXISTS "Kundeordre" (
	"ordreNR"	INTEGER NOT NULL UNIQUE,
	"kjøpsTidspunkt"	INTEGER NOT NULL CHECK("kjøpsTidspunkt" > 0),
	"kundeID"	INTEGER NOT NULL,
	"ruteID"	INTEGER NOT NULL,
	"dato"	INTEGER NOT NULL,
	FOREIGN KEY("ruteID") REFERENCES "TogruteForekomst"("ruteID") ON UPDATE CASCADE,
	FOREIGN KEY("dato") REFERENCES "TogruteForekomst"("dato") ON UPDATE CASCADE,
	FOREIGN KEY("kundeID") REFERENCES "Kunde"("kundeID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("ordreNR" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "GårPåUkedag" (
	"navn"	TEXT NOT NULL,
	"ruteID"	INTEGER NOT NULL,
	FOREIGN KEY("navn") REFERENCES "Ukedag"("navn") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("ruteID") REFERENCES "Togrute"("ruteID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("navn","ruteID")
);
CREATE TABLE IF NOT EXISTS "KjørerStrekning" (
	"ruteID"	INTEGER NOT NULL,
	"delstrekningID"	INTEGER NOT NULL,
	"tidStasjon1"	INTEGER NOT NULL,
	"tidStasjon2"	INTEGER NOT NULL,
	FOREIGN KEY("ruteID") REFERENCES "Togrute"("ruteID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("delstrekningID") REFERENCES "Delstrekning"("delstrekningID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("ruteID","delstrekningID")
);
CREATE TABLE IF NOT EXISTS "HarDelstrekning" (
	"strekningID"	INTEGER NOT NULL,
	"delstrekningID"	INTEGER NOT NULL,
	FOREIGN KEY("strekningID") REFERENCES "Banestrekning"("strekningID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("delstrekningID") REFERENCES "Delstrekning"("delstrekningID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("strekningID","delstrekningID")
);
CREATE TABLE IF NOT EXISTS "HarBillett" (
	"billettID"	INTEGER NOT NULL,
	"vognID"	INTEGER NOT NULL,
	"seteNR"	INTEGER NOT NULL,
	"delstrekningID"	INTEGER NOT NULL,
	FOREIGN KEY("seteNR") REFERENCES "Sete"("seteNR") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("vognID") REFERENCES "Sete"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("billettID") REFERENCES "Setebillett"("billettID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("delstrekningID") REFERENCES "Delstrekning"("delstrekningID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("billettID","vognID","seteNR","delstrekningID")
);
CREATE TABLE IF NOT EXISTS "HarKupeBillett" (
	"billettID"	INTEGER NOT NULL,
	"vognID"	INTEGER NOT NULL,
	"kupeNR"	INTEGER NOT NULL,
	"sengNR"	INTEGER NOT NULL,
	"ruteID"	INTEGER NOT NULL,
	"dato"	INTEGER NOT NULL,
	FOREIGN KEY("sengNR") REFERENCES "Kupebillett"("sengNR") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("vognID") REFERENCES "Kupebillett"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("billettID") REFERENCES "Kupebillett"("billettID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("dato") REFERENCES "TogruteForekomst"("dato") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("kupeNR") REFERENCES "Kupebillett"("kupeNR") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("ruteID") REFERENCES "TogruteForekomst"("ruteID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("billettID","vognID","kupeNR","sengNR","ruteID","dato")
);
CREATE TABLE IF NOT EXISTS "Billett" (
	"billettID"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("billettID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Kupebillett" (
	"billettID"	INTEGER NOT NULL UNIQUE,
	"kupeNR"	INTEGER NOT NULL,
	"sengNR"	INTEGER NOT NULL,
	"vognID"	INTEGER NOT NULL,
	FOREIGN KEY("billettID") REFERENCES "Billett"("billettID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("kupeNR") REFERENCES "Seng"("kupeNR") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("sengNR") REFERENCES "Seng"("sengNR") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("vognID") REFERENCES "Sovevogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("billettID")
);
CREATE TABLE IF NOT EXISTS "Setebillett" (
	"billettID"	INTEGER NOT NULL UNIQUE,
	FOREIGN KEY("billettID") REFERENCES "Billett"("billettID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("billettID")
);
CREATE TABLE IF NOT EXISTS "BillettIOrdre" (
	"ordreNR"	INTEGER NOT NULL,
	"billettID"	INTEGER NOT NULL UNIQUE,
	FOREIGN KEY("ordreNR") REFERENCES "Kundeordre"("ordreNR") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("billettID") REFERENCES "Billett"("billettID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("ordreNR","billettID")
);
CREATE TABLE IF NOT EXISTS "Vogn" (
	"vognID"	INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("vognID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Sovevogn" (
	"vognID"	INTEGER NOT NULL UNIQUE,
	"type"	TEXT NOT NULL,
	FOREIGN KEY("type") REFERENCES "SovevognType"("type") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("vognID") REFERENCES "Vogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("vognID")
);
CREATE TABLE IF NOT EXISTS "Sittevogn" (
	"vognID"	INTEGER NOT NULL UNIQUE,
	"type"	TEXT NOT NULL,
	FOREIGN KEY("type") REFERENCES "SittevognType"("type") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("vognID") REFERENCES "Vogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("vognID")
);
CREATE TABLE IF NOT EXISTS "VognIOppsett" (
	"oppsettID"	INTEGER NOT NULL,
	"vognID"	INTEGER NOT NULL,
	"vognNR"	INTEGER NOT NULL CHECK("vognNR" > 0),
	FOREIGN KEY("vognID") REFERENCES "Vogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("oppsettID") REFERENCES "Vognoppsett"("oppsettID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("oppsettID","vognID")
);
CREATE TABLE IF NOT EXISTS "Kunde" (
	"kundeID"	INTEGER NOT NULL UNIQUE,
	"navn"	TEXT NOT NULL,
	"epost"	TEXT UNIQUE,
	"mobilnr"	INTEGER UNIQUE,
	PRIMARY KEY("kundeID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "HarVogn" (
	"operatørNavn"	TEXT NOT NULL,
	"vognID"	INTEGER NOT NULL UNIQUE,
	FOREIGN KEY("vognID") REFERENCES "Vogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("operatørNavn") REFERENCES "Operatør"("operatørNavn") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("operatørNavn","vognID")
);
CREATE TABLE IF NOT EXISTS "SovevognType" (
	"type"	TEXT NOT NULL UNIQUE,
	"antallKupeer"	INTEGER NOT NULL,
	PRIMARY KEY("type")
);
CREATE TABLE IF NOT EXISTS "Sovekupe" (
	"vognID"	INTEGER NOT NULL,
	"kupeNR"	INTEGER NOT NULL,
	FOREIGN KEY("vognID") REFERENCES "Sovevogn"("vognID") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("vognID", "kupeNR")
);
CREATE TABLE IF NOT EXISTS "Seng" (
	"vognID"	INTEGER NOT NULL,
	"sengNR"	INTEGER NOT NULL,
	"kupeNR"	INTEGER NOT NULL,
	FOREIGN KEY("vognID","kupeNR") REFERENCES "Sovekupe" ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("vognID","sengNR","kupeNR")
);
CREATE TABLE "Togrute" (
	"ruteID"	INTEGER NOT NULL UNIQUE,
	"medHovedRetning"	INTEGER NOT NULL CHECK("medHovedRetning" IN (0, 1)),
	"operatørNavn"	TEXT,
	"oppsettID"	INTEGER NOT NULL,
	"strekningID"	INTEGER NOT NULL,
	PRIMARY KEY("ruteID" AUTOINCREMENT),
	FOREIGN KEY("operatørNavn") REFERENCES "Operatør"("operatørNavn") ON UPDATE CASCADE ON DELETE SET NULL,
	FOREIGN KEY("oppsettID") REFERENCES "Vognoppsett"("oppsettID") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("strekningID") REFERENCES "Banestrekning"("strekningID") ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "Delstrekning" (
	"delstrekningID"	INTEGER NOT NULL UNIQUE,
	"sportype"	TEXT NOT NULL CHECK("sportype" IN ("enkelt", "dobbelt")),
	"lengde"	INTEGER NOT NULL,
	"stasjon1"	TEXT NOT NULL,
	"stasjon2"	TEXT NOT NULL,
	FOREIGN KEY("stasjon2") REFERENCES "Jernbanestasjon"("navn") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("stasjon1") REFERENCES "Jernbanestasjon"("navn") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("delstrekningID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Banestrekning" (
	"strekningID"	INTEGER NOT NULL UNIQUE,
	"navn"	TEXT,
	"fremdriftsenergi"	TEXT NOT NULL CHECK("fremdriftsenergi" IN ("elektrisk", "diesel")),
	"startstasjonNavn"	TEXT NOT NULL,
	"sluttstasjonNavn"	TEXT NOT NULL,
	FOREIGN KEY("sluttstasjonNavn") REFERENCES "Jernbanestasjon"("navn") ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("startstasjonNavn") REFERENCES "Jernbanestasjon"("navn") ON UPDATE CASCADE ON DELETE CASCADE,
	PRIMARY KEY("strekningID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Ukedag" (
	"navn"	TEXT NOT NULL CHECK("navn" IN ("man", "tir", "ons", "tor", "fre", "lør", "søn")) UNIQUE,
	PRIMARY KEY("navn")
);
CREATE TABLE IF NOT EXISTS "SetebillettIOrdre" (
	"billettID"	INTEGER NOT NULL UNIQUE,
	"seteNR"	INTEGER NOT NULL,
	"vognID"	INTEGER NOT NULL,
	"delstrekningID"	INTEGER NOT NULL,
	PRIMARY KEY("billettID","seteNR","vognID","delstrekningID"),
	FOREIGN KEY("delstrekningID") REFERENCES "Delstrekning" ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("seteNR","vognID") REFERENCES "Sete" ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY("billettID") REFERENCES "Billett" ON UPDATE CASCADE ON DELETE CASCADE
);
COMMIT;
