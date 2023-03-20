-- prepares an SQL server assuming it doesnt already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db\g
CREATE USER IF NOT EXISTS hbnb_dev@localhost\g
SET PASSWORD FOR hbnb_dev@localhost = 'hbnb_dev_pwd'\g
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO hbnb_dev@localhost\g
GRANT SELECT ON performance_schema . * TO hbnb_dev@localhost\g
FLUSH PRIVILEGES\g
