import sqlite3
coon=sqlite3.connect("firmi.db")
curs=coon.cursor()

zap1="""CREATE TABLE SPRAVOCHNIK (F_I_O TEXT,YCHINAYA_Stepen TEXT,SINCE_WAY TEXT,MESTO_RABOTI TEXT,
        KAFEDRA TEXT, DOLJNOST TEXT,CONTRY TEXT,CITY TEXT,ADRESS TEXT,PHONE TEXT,MAIL TEXT);"""
zap2="""CREATE TABLE INFO (DOKLADCHIK BOOL,PRIGLASHENIE DATE,TEMA_DOKLADA TEXT,TEZIS TEXT,
        PRIEZD DATE,GOSTINICA BOOL,OTYEZD DATE);"""


zap3="""CREATE TABLE CONFIRENCYA (NAME_CONFIRENCYA TEXT,PROVIDENIYE DATE,MESTO TEXT,ORGONIZATORS TEXT,SPONSORS TEXT,KOLICHESTVO_DAYS INTEGER,
        KOL_PLAYERS INTEGER,KOL_DOKLADCHIKOV INTEGER);"""

curs.execute(zap1)
curs.execute(zap2)
curs.execute(zap3)

coon.commit()

curs.close()
coon.close()