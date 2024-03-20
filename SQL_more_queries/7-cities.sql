-- Creates the table cities in the database hbtn_0d_usa on the MySQL server.

USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT PRIMARY KEY AUTO_INCREMENT,
        state_id INT NOT NULL,
	    name VARCHAR(256),
	        FOREIGN KEY (state_id) REFERENCES states(id)
		);
		
