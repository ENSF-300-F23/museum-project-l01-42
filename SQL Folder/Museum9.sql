drop database if exists museum;
create database museum;
use museum;

create table ART_OBJECT
(obj_ID char(5) not null,
title varchar(50) not null,
descript varchar(70) not null,
year_created int not null,
origin varchar(20) not null,
epoch varchar(20) not null,
collection_name varchar(25),
artist_name varchar(25),
exhibit_ID char(5),

constraint AOPK primary key (obj_ID));

create table PAINTING
(obj_ID char(5) not null,
paint_type varchar(20) not null,
drawn_on varchar(20) not null,
style varchar(20) not null,

constraint PPK primary key (obj_ID),
constraint PFK foreign key (obj_ID) references ART_OBJECT(obj_ID));

create table SCULPTURE
(obj_ID char(5) not null,
material varchar(20) not null,
height_meter varchar(10) not null,
weight_Kg varchar(20) not null,
style varchar(20) not null,

constraint SCPK primary key (obj_ID),
constraint SCFK foreign key (obj_ID) references ART_OBJECT(obj_ID));

create table STATUE
(obj_ID char(5) not null,
material varchar(20) not null,
height_meter varchar(10) not null,
weight_Kg varchar(20) not null,
style varchar(20) not null,

constraint STPK primary key (obj_ID),
constraint STFK foreign key (obj_ID) references ART_OBJECT(obj_ID));

create table OTHER
(obj_ID char(5) not null,
Otype varchar(20) not null,
style varchar(20) not null,

constraint SPK primary key (obj_ID),
constraint OFK foreign key (obj_ID) references ART_OBJECT(obj_ID));

create table COLLECTIONS
(collection_name varchar(25) not null,
Ctype varchar(20) not null,
descript varchar(100) not null,
address varchar(30) not null,
phone char(12) not null,
current_contact varchar(20) not null,

constraint CPK primary key (collection_name));

create table BORROWED_COLLECTION
(borrowed_from varchar(25) not null,
date_returned date,
date_borrowed date not null,

constraint BCPK primary key (borrowed_from),
constraint BCFK foreign key (borrowed_from) references COLLECTIONS(collection_name));

create table PERMANENT_COLLECTION
(collection_name varchar(25) not null,
Pstatus varchar(10) not null,
cost int not null,
date_acquired date not null,

constraint PCPK primary key (collection_name),
constraint PCFK foreign key (collection_name) references COLLECTIONS(collection_name));

create table ARTIST
(artist_name varchar(25),
obj_ID char(5),
descript varchar(50),
date_born date,
date_died date,
country_of_orgin varchar(20) not null,
style varchar(20) not null,
epoch varchar(20) not null,

constraint ARTPK primary key (artist_name, obj_ID),
constraint ARTFK foreign key (obj_ID) references ART_OBJECT(obj_ID));

create table EXHIBITION
(exhibit_ID char(5) not null,
Ename varchar(20) not null,
start_date date not null,
end_date varchar(10) not null,

constraint EXID primary key (exhibit_ID));

insert into EXHIBITION
values 	('90001', 'Cecily Brown', '2023-12-03', '2023-12-10'), 
		('90002', 'Manet Degas', '2023-12-11', '2023-12-18'), 
        ('90003', 'Africa & Byzantium', '2023-12-19', '2023-12-27'), 
		('90004', 'Tentacrome', '2020-11-30', 'Ongoing'); 

insert into ART_OBJECT
values  ('10001', 'Martyrdom of the 7', 'A narrative of religious persecution.', 1530, 'Flemish', 'Renaissance', 'Fletcher Collection', 'Dirck Vellert', '90001'),
		('10002', 'Tric Trac Gameboard', 'Gameboards served as diplomatic gifts.', 1550, 'German', 'Renaissance', 'Fletcher Collection', 'David Schwartz', '90001'),
        ('10003', 'The Death of Dave', 'Showcases the death of St.Dave.', 1250, 'Greek', 'Medieval', 'Fletcher Collection', 'Alexander Antacoumpo', '90001'),
        ('10004', 'Valhalla', 'Showcases the deciding battle for Valhalla.', 793, 'Scandavavian', 'Viking Age', 'Fletcher Collection', null, '90002'),
        ('10005', 'The Statue of Eren', 'A leading Monarch for the People.', 1790, 'Japanese', 'Industrial', 'Brown Collection', null, '90002'),
        ('10006', 'The Statue of Alexander the Great', 'King of Macedon', 320, 'Greek', 'Ancient', 'Brown Collection', null, '90002'),
        ('10007', 'The Bust of Nefertiti', 'Great Royal Wife of Egyptian pharaoh Akhenaten', 350, 'Egypt', 'Ancient', 'Brown Collection', 'Thutmoze', '90002'),
		('10008', 'Guitar', 'An instrument of great influence.', 1910, 'Spain', 'Machine Age', 'Brown Collection', null, '90003'),
        ('10009', 'Bowl', 'A useful item in the Egyptian Age.', 10, 'Egypt', 'Midieval', 'Taisho Collection', null, '90003'),
        ('10010', 'Spoon', 'First invented in the 400s for food.', 420, 'East European', 'Ancient', 'Taisho Collection', null, '90003'),
        ('10011', 'Cup', 'First created in in the 100s for water.', 145, 'France', 'Ancient', 'Taisho Collection', null, '90004'),
        ('10012', 'Slippers', 'First invented in the 200s for transportation.', 220, 'Italy', 'Ancient', 'Contrast Collection', null, '90004'),
        ('10013', 'Apron', 'First invented in the 1700s for royals.', 1740, 'Britian', 'Industrial', 'Contrast Collection', null, '90004'),
        ('10014', 'Barcelona', 'The first painting ever made for Barcelona.', 1640, 'Spain', 'Renaissance', 'Contrast Collection', null, '90004');

insert into PAINTING
values  ('10003', 'Oil', 'Cotton', 'Realism'),
		('10004', 'Incoustic', 'Silk', 'Impressionism'),
        ('10014', 'Oil', 'Leather', 'Realism');

insert into SCULPTURE
values  ('10007', 'Stone', '0.5', '20', 'Round'),
		('10008', 'Marble', '1.1', '40', 'Musical');

insert into STATUE
values  ('10005', 'Stone', '4', '240', 'Carved'),
		('10006', 'Ivory', '6', '640', 'Carved');

insert into OTHER
values  ('10001', 'Stained Glass', 'Glass Stained'),
		('10002', 'Gameboard', 'Entertainment'),
        ('10009', 'Pottery', 'Ancient'),
        ('10010', 'Pottery', 'Ancient'),
        ('10011', 'Pottery', 'Ancient'),
        ('10012', 'Pottery', 'Ancient'),
        ('10013', 'Cloth', 'Royalty');

insert into COLLECTIONS
values  ('Fletcher Collection', 'Museum', 'Collection of pieces regarding personal interests.', '731 Fondren, Houston TX', '111-222-3333', 'James Fletcher'),
		('Brown Collection', 'Museum', 'Collection of pieces regarding past Leaders.', '291 Berry, Bellaire TX', '222-333-4444', 'Bruce Brown'),
        ('Taisho Collection', 'Personal', 'Collection of pieces regarding ancient items.', '5631 Rice, Houston TX', '333-444-5555', 'Nick Suzuki'),
        ('Contrast Collection', 'Personal', 'Collection of pieces regarding valuable inventions.', '980 Dallas, Houston TX', '444-555-6666', 'Henry Bucklemore');

insert into BORROWED_COLLECTION
values  ('Taisho Collection', '2023-07-21', '2020-01-13'),
		('Contrast Collection', null, '2015-09-22');

insert into PERMANENT_COLLECTION
values  ('Fletcher Collection', 'On Display', 300000, '2002-08-19'),
		('Brown Collection', 'Stored', 815000, '2010-03-10');

insert into ARTIST
values  ('Dirck Vellert', '10001','World-Renouned Artist of the Renaissance', '1489-05-04', '1559-12-03', 'Belgium', 'Futurism', 'Renaissance'),
		('David Schwartz','10002', 'Small German Artist of the Renaissance', null, null, 'Germany', 'Rococo', 'Renaissance'),
        ('Alexander Antacoumpo', '10003', 'Famed Painter of the Medieval times', '1220-02-24', '1287-01-31', 'Greece', 'Classicism', 'Medieval'),
        ('Thutmoze','10007', null, null, null, 'Egypt', 'Symbolism', 'Medieval');

alter table ART_OBJECT
	add constraint CFK foreign key (collection_name) references COLLECTIONS(collection_name),
    add constraint EIDFK foreign key (exhibit_ID) references EXHIBITION(exhibit_ID),
	add constraint AFK foreign key (artist_name) references ARTIST(artist_name);

-- Deletion Constraints 
-- For the foreign key referencing COLLECTIONS
ALTER TABLE ART_OBJECT
    DROP FOREIGN KEY CFK; -- Drop the existing constraint
ALTER TABLE ART_OBJECT
    ADD CONSTRAINT CFK
    FOREIGN KEY (collection_name)
    REFERENCES COLLECTIONS(collection_name)
    ON DELETE cascade;

-- For the foreign key referencing EXHIBITION
ALTER TABLE ART_OBJECT
    DROP FOREIGN KEY EIDFK;
ALTER TABLE ART_OBJECT
    ADD CONSTRAINT EIDFK
    FOREIGN KEY (exhibit_ID)
    REFERENCES EXHIBITION(exhibit_ID)
    ON DELETE cascade;

-- For the foreign key referencing ARTIST
ALTER TABLE ART_OBJECT
    DROP FOREIGN KEY AFK;
ALTER TABLE ART_OBJECT
    ADD CONSTRAINT AFK
    FOREIGN KEY (artist_name)
    REFERENCES ARTIST(artist_name)
    ON DELETE cascade;

-- For the foreign key referencing ART_OBJECT
ALTER TABLE PAINTING
    DROP FOREIGN KEY PFK; -- Drop the existing constraint
ALTER TABLE PAINTING
    ADD CONSTRAINT PFK
    FOREIGN KEY (obj_ID)
    REFERENCES ART_OBJECT(obj_ID)
    ON DELETE cascade;

-- For the foreign key referencing ART_OBJECT
ALTER TABLE SCULPTURE
    DROP FOREIGN KEY SCFK; -- Drop the existing constraint
ALTER TABLE SCULPTURE
    ADD CONSTRAINT SCFK
    FOREIGN KEY (obj_ID)
    REFERENCES ART_OBJECT(obj_ID)
    ON DELETE cascade;

ALTER TABLE STATUE
    DROP FOREIGN KEY STFK; -- Drop the existing constraint
ALTER TABLE STATUE
    ADD CONSTRAINT STFK
    FOREIGN KEY (obj_ID)
    REFERENCES ART_OBJECT(obj_ID)
    ON DELETE cascade;

ALTER TABLE OTHER
    DROP FOREIGN KEY OFK; -- Drop the existing constraint
ALTER TABLE OTHER
    ADD CONSTRAINT OFK
    FOREIGN KEY (obj_ID)
    REFERENCES ART_OBJECT(obj_ID)
    ON DELETE cascade;

ALTER TABLE artist
DROP FOREIGN KEY ARTFK;

ALTER TABLE artist
ADD CONSTRAINT ARTFK
FOREIGN KEY (obj_ID)
REFERENCES art_object(obj_ID)
ON DELETE CASCADE;





