drop database if exists museum;
create database museum;
use museum;

create table ART_OBJECT
(obj_ID char(5) not null,
title varchar(50) not null,
descript varchar(50) not null,
year_created char(4) not null,
origin varchar(20) not null,
epoch varchar(20) not null,
collection_name varchar(25) not null,

constraint AOPK primary key (obj_ID));

create table SCULPTURE
(obj_ID char(5) not null,
material varchar(20) not null,
height_meter varchar(10) not null,
weight_Kg varchar(20) not null,
style varchar(20) not null,

constraint SCPK primary key (obj_ID));

create table STATUE
(obj_ID char(5) not null,
material varchar(20) not null,
height_meter varchar(10) not null,
weight_Kg varchar(20) not null,
style varchar(20) not null,

constraint STPK primary key (obj_ID));

create table OTHER
(obj_ID char(5) not null,
Otype varchar(20) not null,
style varchar(20) not null,

constraint SPK primary key (obj_ID));

create table COLLECTIONS
(collection_name varchar(25) not null,
Ctype varchar(20) not null,
descript varchar(50) not null,
address varchar(30) not null,
phone char(12) not null,
current_contact varchar(20) not null,

constraint CPK primary key (collection_name));

create table BORROWED_COLLECTION
(collection_name varchar(25) not null,
date_returned date,
date_borrowed date not null,
borrowed_from varchar(20) not null,

constraint BCPK primary key (collection_name));

create table PERMANENT_COLLECTION
(collection_name varchar(25) not null,
Pstatus varchar(10) not null,
cost int(10) not null,
date_acquired date not null,

constraint PCPK primary key (collection_name));

create table ARTIST
(artist_name varchar(25) not null,
descript varchar(50),
date_born date,
dat_died date,
country_of_orgin varchar(20) not null,
style varchar(20) not null,
epoch varchar(20) not null,

constraint ARTPK primary key (artist_name));

create table EXHIBITION
(exhibit_ID char(5) not null,
Ename varchar(20) not null,
start_date date not null,
end_date date not null,

constraint EXID primary key (exhibit_ID));
