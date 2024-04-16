-- Prepares a MySQL server for user hbnb_test and hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFY BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbhb_test'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
