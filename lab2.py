import sqlite3
coon=sqlite3.connect("firmi.db")
curs=coon.cursor()

#zap1="""CREATE TABLE SPRAVOCHNIK (F_I_O TEXT,YCHINAYA_Stepen TEXT,SINCE_WAY TEXT,MESTO_RABOTI TEXT,
  #      KAFEDRA TEXT, DOLJNOST TEXT,CONTRY TEXT,CITY TEXT,ADRESS TEXT,PHONE TEXT,MAIL TEXT);"""
#zap2="""CREATE TABLE INFO (DOKLADCHIK BOOL,PRIGLASHENIE DATE,TEMA_DOKLADA TEXT,TEZIS TEXT,
      #  PRIEZD DATE,GOSTINICA BOOL,OTYEZD DATE);"""
zap3="""CREATE TABLE CONFIRENCYA (NAME_CONFIRENCYA TEXT,PROVIDENIYE DATE,MESTO TEXT,ORGONIZATORS TEXT,SPONSORS TEXT,KOLICHESTVO_DAYS INTEGER,
        KOL_PLAYERS INTEGER,KOL_DOKLADCHIKOV INTEGER);"""
insert1="""INSERT INTO INFO VALUES (TRUE,'04.02.2022','Прагматика новостных текстов','знакомство с новой методикой Подробнее','04.03.2022',FALSE,'04.04.2022');"""
insert2="""INSERT INTO INFO VALUES (FALSE,'06.12.2022','СМИ-рекламоносители: преимущества и недостатки','традиции и современность','04.01.2023',FALSE,'04.02.2023');"""
insert3="""INSERT INTO INFO VALUES (TRUE,'29.10.2022','Методы описания рекламных текстов','дискурс ориентализма и его критика','29.11.2022',TRUE,'29.12.2022');"""
insert4="""INSERT INTO INFO VALUES (TRUE,'02.06.2023','Образ России в зарубежных СМИ','основные гипотезы и общие положения','02.07.2023',FALSE,'02.08.2023');"""
insert5="""INSERT INTO INFO VALUES (TRUE,'04.03.2023','Case study – особенности освещения конкретного события различными СМИ','приведение промежуточных результатов, их анализ','04.04.2023',TRUE,'04.05.2023');"""
insert6="""INSERT INTO INFO VALUES (FALSE,'26.03.2023','Технологии дискурсивного анализа в изучении текстов массовой информации','расчетные данные','26.04.2023',TRUE,'26.05.2023');"""
'''
insert1="""INSERT INTO CONFIRENCYA VALUES ('Наука и Просвещение','04.01.2023','Абхазия','adstars',
'Российского Фонда Фундаментальных Исследований РФФИ',7,213,20);"""
insert2="""INSERT INTO CONFIRENCYA VALUES ('Актуальные вопросы общества, науки и образования','26.04.2022','Китай',
'adstars','Российского Фонда Фундаментальных Исследований РФФИ',14,70,7);"""
insert3="""INSERT INTO CONFIRENCYA VALUES ('Современные научные знания','28.08.2021','Израиль','adstars',
'Российского Фонда Фундаментальных Исследований РФФИ',3,297,26);"""
insert4="""INSERT INTO CONFIRENCYA VALUES ('Молодёжная наука','28.01.2023','Армения','adstars',
'Российского Фонда Фундаментальных Исследований РФФИ',4,47,5);"""
insert5="""INSERT INTO CONFIRENCYA VALUES ('Современная наука и образование: актуальные вопросы теории и практики',
'29.08.2021','Ватикан','adstars','Российского Фонда Фундаментальных Исследований РФФИ',1,177,13);"""
insert6="""INSERT INTO CONFIRENCYA VALUES ('оссийская наука в современном мире','28.01.2023','Япония','adstars',
'Российского Фонда Фундаментальных Исследований РФФИ',3,111,11);"""
insert1="""INSERT INTO SPRAVOCHNIK VALUES ('Корхов Александр Игоревич','Доктор наук','Биология','Научный центр',
        'Биологии', 'Главный руководитель','Беларусь','Минск','ул.Немига 5','+375291829805','amuvie@mail.ru');"""
insert2="""INSERT INTO SPRAVOCHNIK VALUES ('Борисова Стефания Михайловна','Кандидат наук','Физика','Научный центр',
        'Физика', 'Ученый','Бурунди','Гитега','ул.Немига 5','+375291829805','amuvie@mail.ru');"""
insert3="""INSERT INTO SPRAVOCHNIK VALUES ('Пономарева Евангелина Артёмовна','Бакалавр ','Химия','Научный центр',
        'Химия', 'научный работник','Вануату','Порт-Вила','Тбилисская улица 37','+50(22)527-95-21','naxaheidequou-1260@yopmail.com');"""
insert4="""INSERT INTO SPRAVOCHNIK VALUES ('Миронов Александр Яромирович','Бакалавр ','Экономические науки','Научный центр',
        'Экономические науки', 'Ученый ','Гана','Аккра','Жилуновича улица 128','+375291829805','kounnilinneinno-3471@yopmail.com');"""
insert5="""INSERT INTO SPRAVOCHNIK VALUES ('Ермилова Диана Константиновна','Магистр ','Биология','Научный центр',
        'Биологии', 'Главный руководитель','Израиль','Иерусалим','Заборского улица 97','+66(7334)718-39-84','trallerassare-4523@yopmail.com');"""
insert6="""INSERT INTO SPRAVOCHNIK VALUES ('Коновалов Алексей Дмитриевич','Кандидат наук','Литература','Научный центр',
        'Литература', 'научный работник','Исландия','Рейкьявик','Светлая улица 27','+762(3464)146-06-17','brubremapoupro-3224@yopmail.com');"""
    '''

curs.execute(insert1)
curs.execute(insert2)
curs.execute(insert3)
curs.execute(insert4)
curs.execute(insert5)
curs.execute(insert6)


coon.commit()

curs.close()
coon.close()