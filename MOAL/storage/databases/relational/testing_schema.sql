create database if not exists mytestdb;

-- drop table if exists mytestdb.person;
-- drop table if exists mytestdb.relationship;

create table if not exists mytestdb.person (
    id int not null auto_increment,
    name varchar(255),
    age int,
    dob varchar(10),
    primary key (id)
);

create table if not exists mytestdb.relationship (
    id int not null auto_increment,
    person_id int,
    index per_id (person_id),
    foreign key (id)
        references person(id)
        on update cascade,
    relation_name varchar(255),
    primary key (id)
);

insert into mytestdb.person values(1, 'chris', 29, '01/05/1986');
insert into mytestdb.person values(2, 'lindsey', 29, '02/10/1986');
insert into mytestdb.person values(3, 'ella', 1, '10/13/2014');

insert into mytestdb.relationship values(1, 1, 'father');
insert into mytestdb.relationship values(2, 2, 'mother');
insert into mytestdb.relationship values(3, 3, 'daughter');

call mytestdb.get_by_name('ella');
call mytestdb.get_by_name('chris');

call mytestdb.get_by_age_range(10, 30);
call mytestdb.get_by_age_range(0, 2);
