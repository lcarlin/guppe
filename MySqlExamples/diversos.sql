create database pdw ;
use pdw
create user 'xcprd01'@'localhost' IDENTIFIED BY 'senha';
GRANT ALL PRIVILEGES ON * . * TO 'xcprd01'@'localhost'  ;
FLUSH PRIVILEGES;
/*
sqlite3 sample.db .dump > dump.sql
mysql -p -u xcprd01 -h 127.0.0.1 pdw < dump.sql
*/
show processlist;
show databases ; 
 
use loja_virtual ; 
create table categoria (id int auto_increment, nome varchar(50) not null , primary key (id)) engine = InnoDB ;

insert into CATEGORIA(nome) values ('ELETRONICOS'); 

SELECT * FROM categoria;

ALTER TABLE PRODUTO ADD COLUMN CATEGORIA_ID INT ; 

ALTER TABLE PRODUTO ADD foreign key (CATEGORIA_ID) references CATEGORIA(ID) ; 

COMMIT ; 

SELECT * FROM PRODUTO;

SELECT * FROM categoria;

UPDATE PRODUTO SET CATEGORIA_ID = 1 WHERE ID = 1 ; 
UPDATE PRODUTO SET CATEGORIA_ID = 2 WHERE ID = 2 ; 
UPDATE PRODUTO SET CATEGORIA_ID = 1 WHERE ID = 3 ; 
UPDATE PRODUTO SET CATEGORIA_ID = 3 WHERE ID = 30 ; 
UPDATE PRODUTO SET CATEGORIA_ID = 3 WHERE ID = 31 ; 
UPDATE categoria set nome = 'ELETRONICOS' where id = 1; 

UPDATE categoria set nome = 'ELETRODOMESTICOS' where id = 3; 