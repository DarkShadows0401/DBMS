USE mydata;
CREATE TABLE tablet(
	Name_of_Tablets varchar(50) NOT NULL
);
DELIMITER \\
CREATE TRIGGER addtablets before update on hospital 
for each row
begin
insert into tablet values(hospital.Name_of_Tablets);
end\\
delimiter ;