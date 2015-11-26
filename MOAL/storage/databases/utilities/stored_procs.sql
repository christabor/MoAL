-- SEE ../testing_schema.sql for schema to run with these sprocs.

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `new_procedure`(given_name VARCHAR(255))
BEGIN
    select * from person p where p.name like(given_name);
END

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `new_procedure`(min_age int, max_age int)
BEGIN
    select * from person p where p.age <= max_age and p.age >= min_age;
END
