import sqlite3
coon=sqlite3.connect("firmi.db")
curs=coon.cursor()

zap1="""SELECT * FROM INFO;"""
zap2="""SELECT * FROM CONFIRENCYA;"""
zap3="""SELECT * FROM SPRAVOCHNIK;"""

curs.execute(zap1)
vyb=curs.fetchone()
while vyb:
    print(vyb)
    vyb = curs.fetchone()
curs.execute(zap2)
vyb=curs.fetchone()
while vyb:
    print(vyb)
    vyb = curs.fetchone()
curs.execute(zap3)
vyb=curs.fetchone()
while vyb:
    print(vyb)
    vyb = curs.fetchone()
zap4="""SELECT * FROM SPRAVOCHNIK WHERE SPRAVOCHNIK.CONTRY='Беларусь';"""
curs.execute(zap4)
vyb=curs.fetchone()
while vyb:
    print(vyb)
    vyb = curs.fetchone()
coon.commit()
curs.close()
coon.close()