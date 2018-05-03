create database vocabulary;
use vocabulary;
create table vocabulary(
	ID int,
	word varchar(225),
	meaning nvarchar(225),
	datetime datetime default current_timestamp on update current_timestamp
);
insert into vocabulary (ID, word, meaning, datetime) values (1,"start","開始",default);
