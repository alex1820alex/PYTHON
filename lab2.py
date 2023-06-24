import sqlite3
coon=sqlite3.connect("firmi.db")
curs=coon.cursor()
'''
zap1="""UPDATE  SPRAVOCHNIK SET CONTRY='Польша'  WHERE SPRAVOCHNIK.CONTRY='Беларусь';"""
zap2="""UPDATE  SPRAVOCHNIK SET SINCE_WAY='Математика'  WHERE SPRAVOCHNIK.SINCE_WAY='Биология';"""
zap3="""UPDATE  SPRAVOCHNIK SET MESTO_RABOTI='Гараж'  WHERE SPRAVOCHNIK.MESTO_RABOTI='Научный центр';"""
zap1="""DELETE FROM SPRAVOCHNIK  WHERE SPRAVOCHNIK.F_I_O='Коновалов Алексей Дмитриевич';"""
zap2="""DELETE FROM SPRAVOCHNIK  WHERE SPRAVOCHNIK.F_I_O='Миронов Александр Яромирович';"""
zap3="""DELETE FROM SPRAVOCHNIK  WHERE SPRAVOCHNIK.F_I_O='Пономарева Евангелина Артёмовна';"""

zap1="""UPDATE  INFO SET DOKLADCHIK='1'  WHERE INFO.DOKLADCHIK=TRUE;"""
zap2="""UPDATE  INFO SET TEZIS='LOL'  WHERE INFO.TEZIS='традиции и современность';"""
zap3="""DELETE FROM INFO  WHERE INFO.GOSTINICA=1;"""
'''
zap1="""UPDATE  CONFIRENCYA SET ORGONIZATORS='adstars.2.0'  WHERE CONFIRENCYA.ORGONIZATORS='adstars';"""
zap2="""DELETE FROM CONFIRENCYA  WHERE CONFIRENCYA.KOLICHESTVO_DAYS<4;"""


curs.execute(zap1)
curs.execute(zap2)
coon.commit()
curs.close()
coon.close()