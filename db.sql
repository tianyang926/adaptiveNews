CREATE TABLE Persons(
	UserId int AUTO_INCREMENT NOT NULL,
	UserPassword varchar(255) NOT NULL,
	UserName varchar(255) NOT NULL,
	UserAge int NOT NULL,
	UserGender varchar(255) NOT NULL,
	PRIMARY KEY (UserId)
);