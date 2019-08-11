-- set up development database

-- create the database
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- create the user to administer the database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'
IDENTIFIED BY 'hbnb_dev_pwd';

-- give the user full control over the database
GRANT ALL ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- let the user see the performance data
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
