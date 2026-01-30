-- CREATE TABLE statements for MySQL. If you use SQLite, the app will create equivalent tables automatically.
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(100) PRIMARY KEY,
    hashed_password TEXT NOT NULL,
    role VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS queries (
    query_id INT AUTO_INCREMENT PRIMARY KEY,
    mail_id VARCHAR(255),
    mobile_number VARCHAR(50),
    query_heading TEXT,
    query_description TEXT,
    status VARCHAR(20),
    query_created_time DATETIME,
    query_closed_time DATETIME,
    image LONGBLOB
);
