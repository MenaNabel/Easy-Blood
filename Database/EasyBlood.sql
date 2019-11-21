create database EasyBlood default CHARACTER set UTF8  default collate UTF8_GENERAL_CI;
use EasyBlood;
create table Donors(
ID int primary Key,
UserName varchar (150) unique ,
E_Mail varchar(150) ,
Phone varchar (100),
City varchar(150),
BloodGroup varchar(50),
Wight DOUBLE,
Age int ,
Gender varchar(50),
DataOfLastDonation date
     
);

create table Donors_Cities(
ID_City int primary key ,
City varchar(100),
ID_Donor int ,foreign key(ID_Donor) references Donors(ID)
);
create table Donors_Schedule(
ID_Schedule int primary key,
Status boolean ,
DataOfLastDonation date,
ID_Donor int ,foreign key(ID_Donor) references Donors(ID)
);

create table Needys(
ID_Needy int primary key ,
Name varchar(150) unique,
City varchar (150),
Age double ,
BloodGroup varchar(50),
Hospital varchar(100),
ID_Donor int ,foreign key(ID_Donor)references Donors(ID)
);
